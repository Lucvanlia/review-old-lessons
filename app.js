/**
 * EduPrep.vn - Main JavaScript Application Logic
 * Pure Vanilla JavaScript (No Frameworks)
 */

// Global Application State
// Test hook for automated test environments
if (window.location.search.includes('test=true')) {
    window.confirm = () => true;
}

const state = {
    subjects: [],             // List of all subjects from subjects.json
    currentSubjectId: '',     // Selected subject ID
    currentSubject: null,     // Selected subject details
    knowledgeData: [],        // Knowledge topics for selected subject
    questionsData: [],        // Questions database for selected subject
    presetExams: [],          // Preset mock exams for selected subject
    
    // UI Panel States
    currentPanel: 'home',     
    selectedTopicId: null,    // Active topic index in Knowledge View

    // Quiz (Practice Mode) State
    quiz: {
        active: false,
        selectedTopics: [],
        questions: [],
        currentIndex: 0,
        score: 0,
        userAnswers: [],      // Array of string answers
        checked: false        // Has the current question been checked
    },

    // Mock Exam State
    mock: {
        active: false,
        questions: [],
        currentIndex: 0,
        userAnswers: {},      // Map of questionIndex -> optionIndex/Value
        timer: 0,             // Remaining seconds
        timerInterval: null,
        totalTime: 0,         // Initial seconds
        startTime: null
    }
};

// LocalStorage Keys Helper
const storage = {
    getStatsKey: (subjectId) => `eduprep_stats_${subjectId}`,
    getReadTopicsKey: (subjectId) => `eduprep_read_${subjectId}`,
    getNoteKey: (subjectId, topicId) => `eduprep_note_${subjectId}_${topicId}`,
    getActiveSubjectKey: () => 'eduprep_active_subject',
    
    // Core statistics save/load
    loadStats: (subjectId) => {
        const data = localStorage.getItem(storage.getStatsKey(subjectId));
        return data ? JSON.parse(data) : {
            quizzesTaken: 0,
            mockTaken: 0,
            mockScores: [], // array of percentages
            topicStats: {}  // { topicId: { correct: N, total: M } }
        };
    },
    saveStats: (subjectId, stats) => {
        localStorage.setItem(storage.getStatsKey(subjectId), JSON.stringify(stats));
    },
    
    // Read status
    loadReadTopics: (subjectId) => {
        const data = localStorage.getItem(storage.getReadTopicsKey(subjectId));
        return data ? JSON.parse(data) : [];
    },
    saveReadTopics: (subjectId, readList) => {
        localStorage.setItem(storage.getReadTopicsKey(subjectId), JSON.stringify(readList));
    }
};

// ==========================================================================
// INITIALIZATION
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

async function initApp() {
    setupEventListeners();
    setupRouting();
    
    // Load subjects registry
    try {
        const response = await fetch(`data/subjects.json?t=${Date.now()}`);
        if (!response.ok) throw new Error('Không thể tải tệp subjects.json');
        state.subjects = cleanObjectText(await response.json());
        
        // Populate subject selectors in UI
        populateSubjectDropdown();
        
        // Load default or previously active subject
        const savedSubjectId = localStorage.getItem(storage.getActiveSubjectKey());
        const defaultSubjectId = savedSubjectId && state.subjects.some(s => s.id === savedSubjectId) 
            ? savedSubjectId 
            : (state.subjects.length > 0 ? state.subjects[0].id : '');
            
        if (defaultSubjectId) {
            await selectSubject(defaultSubjectId);
        } else {
            showToast('Chưa cấu hình môn học nào.', 'warning');
        }
    } catch (error) {
        console.error('Lỗi khởi tạo ứng dụng:', error);
        showToast('Lỗi tải dữ liệu ứng dụng. Vui lòng chạy trên Local Server!', 'danger');
    }
}

// ==========================================================================
// EVENT LISTENERS & SIDEBAR HANDLERS
// ==========================================================================
function setupEventListeners() {
    // Initialize Custom Premium Selects
    initCustomSelects();

    // Mobile Sidebar Toggles
    const menuToggle = document.getElementById('menu-toggle-trigger');
    const closeSidebar = document.getElementById('close-sidebar-trigger');
    const sidebar = document.getElementById('app-sidebar');
    
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', () => {
            sidebar.classList.add('mobile-active');
        });
    }
    
    if (closeSidebar && sidebar) {
        closeSidebar.addEventListener('click', () => {
            sidebar.classList.remove('mobile-active');
        });
    }

    // Sidebar Navigation Click Handlers (For responsive overlay close)
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            if (sidebar) sidebar.classList.remove('mobile-active');
        });
    });

    // Subject Dropdown Selector in Sidebar
    const subjectDropdown = document.getElementById('sidebar-subject-select');
    if (subjectDropdown) {
        subjectDropdown.addEventListener('change', async (e) => {
            const subjectId = e.target.value;
            if (subjectId) {
                await selectSubject(subjectId);
                // Redirect back to home to see new subject details
                window.location.hash = '#home';
            }
        });
    }

    // Practice Setup Actions
    const btnSelectAll = document.getElementById('btn-select-all-topics');
    const btnDeselectAll = document.getElementById('btn-deselect-all-topics');
    
    if (btnSelectAll) {
        btnSelectAll.addEventListener('click', () => toggleAllTopicCheckboxes(true));
    }
    if (btnDeselectAll) {
        btnDeselectAll.addEventListener('click', () => toggleAllTopicCheckboxes(false));
    }

    const btnStartPractice = document.getElementById('btn-start-practice');
    if (btnStartPractice) {
        btnStartPractice.addEventListener('click', startPracticeQuiz);
    }

    const btnQuitQuiz = document.getElementById('btn-quit-quiz');
    if (btnQuitQuiz) {
        btnQuitQuiz.addEventListener('click', quitPracticeQuiz);
    }

    const btnNextQuestion = document.getElementById('btn-next-question');
    if (btnNextQuestion) {
        btnNextQuestion.addEventListener('click', handleNextQuizQuestion);
    }

    // Mock Test Setup Actions
    const btnStartMock = document.getElementById('btn-start-mock');
    if (btnStartMock) {
        btnStartMock.addEventListener('click', startMockExam);
    }

    const mockExamTypeSelect = document.getElementById('mock-exam-type-select');
    if (mockExamTypeSelect) {
        mockExamTypeSelect.addEventListener('change', (e) => {
            const qtyGroup = document.getElementById('mock-qty-selection-group');
            if (qtyGroup) {
                if (e.target.value === 'random') {
                    qtyGroup.classList.remove('hidden');
                } else {
                    qtyGroup.classList.add('hidden');
                }
            }
        });
    }

    const btnMockPrev = document.getElementById('btn-mock-prev');
    const btnMockNext = document.getElementById('btn-mock-next');
    if (btnMockPrev) {
        btnMockPrev.addEventListener('click', () => navigateMockQuestion(-1));
    }
    if (btnMockNext) {
        btnMockNext.addEventListener('click', () => navigateMockQuestion(1));
    }

    document.addEventListener('click', (e) => {
        const btnSubmit = e.target.closest('#btn-submit-mock');
        if (btnSubmit) {
            submitMockExam(false);
        }
    });

    // Results Redirections
    const btnResultToAnalytics = document.getElementById('btn-result-to-analytics');
    const btnResultToHome = document.getElementById('btn-result-to-home');
    if (btnResultToAnalytics) {
        btnResultToAnalytics.addEventListener('click', () => {
            window.location.hash = '#analytics';
        });
    }
    if (btnResultToHome) {
        btnResultToHome.addEventListener('click', () => {
            window.location.hash = '#home';
        });
    }
}

// ==========================================================================
// ROUTING SYSTEM (SPA)
// ==========================================================================
function setupRouting() {
    window.addEventListener('hashchange', handleRoute);
    // Trigger on initial load
    handleRoute();
}

function handleRoute() {
    const hash = window.location.hash || '#home';
    const panelId = hash.replace('#', '');
    
    // Check if panels exist and clean active classes
    const panels = document.querySelectorAll('.panel');
    const navItems = document.querySelectorAll('.nav-item');
    
    let targetPanel = document.getElementById(`panel-${panelId}`);
    let targetNav = document.getElementById(`nav-${panelId}`);
    
    // Handle specific mappings
    if (panelId === 'mock-test') {
        targetPanel = document.getElementById('panel-mock');
        targetNav = document.getElementById('nav-mock');
    }
    
    if (targetPanel) {
        panels.forEach(p => p.classList.remove('active'));
        targetPanel.classList.add('active');
        
        navItems.forEach(n => n.classList.remove('active'));
        if (targetNav) targetNav.classList.add('active');
        
        state.currentPanel = panelId;
        
        // Update top navbar page title
        updatePageTitle(panelId);
        
        // Perform panel specific activation logics
        onPanelActivated(panelId);
    } else {
        // Fallback to home
        window.location.hash = '#home';
    }
}

function updatePageTitle(panelId) {
    const titleEl = document.getElementById('current-page-title');
    if (!titleEl) return;
    
    const titles = {
        'home': 'Bảng điều khiển',
        'knowledge': 'Tổng hợp kiến thức',
        'practice': 'Luyện tập theo chủ đề',
        'interactive-practice': 'Tự luận vẽ đồ thị AND-OR',
        'mock-test': 'Thi thử tổng hợp',
        'analytics': 'Phân tích học tập'
    };
    
    titleEl.textContent = titles[panelId] || 'Học tập trực tuyến';
}

function onPanelActivated(panelId) {
    // If user leaves active quiz or mock, clean state
    if (panelId !== 'practice' && state.quiz.active) {
        quitPracticeQuiz();
    }
    if (panelId !== 'mock-test' && state.mock.active) {
        // Alert if in mock test
        const confirmExit = confirm('Bạn đang làm bài thi thử. Rời khỏi trang sẽ hủy bài thi hiện tại. Bạn có chắc muốn rời đi?');
        if (confirmExit) {
            clearMockTimer();
            state.mock.active = false;
            document.getElementById('mock-exam-workspace-container').classList.add('hidden');
            document.getElementById('mock-setup-card').classList.remove('hidden');
        } else {
            // Revert route back to mock-test
            window.removeEventListener('hashchange', handleRoute);
            window.location.hash = '#mock-test';
            setTimeout(() => {
                window.addEventListener('hashchange', handleRoute);
            }, 50);
            return;
        }
    }

    // Refresh contents
    if (panelId === 'home') {
        renderHomeScreen();
    } else if (panelId === 'knowledge') {
        renderKnowledgeScreen();
    } else if (panelId === 'practice') {
        renderPracticeSetupScreen();
    } else if (panelId === 'interactive-practice') {
        renderInteractivePracticeScreen();
    } else if (panelId === 'analytics') {
        renderAnalyticsScreen();
    }
}

// ==========================================================================
// SUBJECT LOADING AND SELECTION
// ==========================================================================
function populateSubjectDropdown() {
    const dropdown = document.getElementById('sidebar-subject-select');
    if (!dropdown) return;
    
    dropdown.innerHTML = '';
    state.subjects.forEach(subject => {
        const option = document.createElement('option');
        option.value = subject.id;
        option.textContent = subject.name;
        dropdown.appendChild(option);
    });
    
    // Sync Custom Select UI
    syncCustomSelect('sidebar-subject-select');
}

async function selectSubject(subjectId) {
    state.currentSubjectId = subjectId;
    state.currentSubject = state.subjects.find(s => s.id === subjectId);
    localStorage.setItem(storage.getActiveSubjectKey(), subjectId);
    
    // Update Sidebar dropdown selection value
    const dropdown = document.getElementById('sidebar-subject-select');
    if (dropdown) {
        dropdown.value = subjectId;
        syncCustomSelect('sidebar-subject-select');
    }
    
    // Load data files for this subject
    try {
        const knowledgeRes = await fetch(`data/${subjectId}/knowledge.json?t=${Date.now()}`);
        const questionsRes = await fetch(`data/${subjectId}/questions.json?t=${Date.now()}`);
        
        if (!knowledgeRes.ok || !questionsRes.ok) {
            throw new Error('Không thể tải các tệp tin dữ liệu môn học');
        }
        
        state.knowledgeData = cleanObjectText(await knowledgeRes.json());
        state.questionsData = cleanObjectText(await questionsRes.json());
        
        // Load preset exams if available
        try {
            const presetRes = await fetch(`data/${subjectId}/preset_exams.json?t=${Date.now()}`);
            if (presetRes.ok) {
                state.presetExams = cleanObjectText(await presetRes.json());
            } else {
                state.presetExams = [];
            }
        } catch (e) {
            console.warn(`Không tìm thấy preset_exams.json cho môn học ${subjectId}:`, e);
            state.presetExams = [];
        }
        
        // Split National Defense topics if they have more than 40 questions
        if (subjectId.startsWith('quocphong')) {
            const maxQuestionsPerTopic = 20;
            const newKnowledgeData = [];
            const questionsByTopic = {};
            
            state.questionsData.forEach(q => {
                if (!questionsByTopic[q.topicId]) {
                    questionsByTopic[q.topicId] = [];
                }
                questionsByTopic[q.topicId].push(q);
            });
            
            state.knowledgeData.forEach(topic => {
                const tQuestions = questionsByTopic[topic.topicId] || [];
                const N = tQuestions.length;
                
                if (N > 40) {
                    const numParts = Math.ceil(N / maxQuestionsPerTopic);
                    for (let i = 0; i < numParts; i++) {
                        const partId = `${topic.topicId}_part_${i + 1}`;
                        const startIdx = i * maxQuestionsPerTopic;
                        const endIdx = Math.min(startIdx + maxQuestionsPerTopic, N);
                        const partQuestions = tQuestions.slice(startIdx, endIdx);
                        
                        partQuestions.forEach(q => {
                            q.topicId = partId;
                        });
                        
                        newKnowledgeData.push({
                            topicId: partId,
                            title: `${topic.title} - Phần ${i + 1}`,
                            keywords: topic.keywords || [],
                            summary: topic.summary || '',
                            content: topic.content || '',
                            example: topic.example || ''
                        });
                    }
                } else {
                    newKnowledgeData.push(topic);
                }
            });
            
            state.knowledgeData = newKnowledgeData;
        }
        
        // Update mock exam dropdown in UI
        populateMockExamDropdown();
        
        // Reset navigation states
        state.selectedTopicId = state.knowledgeData.length > 0 ? state.knowledgeData[0].topicId : null;
        
        // Update global progress bar UI
        updateGlobalProgressBar();
        
        // Refresh active screen contents
        onPanelActivated(state.currentPanel);
        
        showToast(`Đã tải môn học: ${state.currentSubject.name}`, 'success');
    } catch (error) {
        console.error(`Lỗi tải dữ liệu môn học ${subjectId}:`, error);
        showToast('Lỗi tải dữ liệu môn học. Vui lòng kiểm tra lại cấu trúc file!', 'danger');
    }
}

function startPracticeForTopic(topicId) {
    state.quiz.selectedTopics = [topicId];
    state.quiz.active = true;
    
    let questions = state.questionsData.filter(q => state.quiz.selectedTopics.includes(q.topicId));
    
    if (questions.length === 0) {
        showToast('Không tìm thấy câu hỏi nào thuộc chủ đề đã chọn!', 'warning');
        state.quiz.active = false;
        return;
    }
    
    state.quiz.questions = shuffleArray([...questions]);
    state.quiz.currentIndex = 0;
    state.quiz.score = 0;
    state.quiz.userAnswers = [];
    state.quiz.checked = false;
    
    window.location.hash = '#practice';
    
    document.getElementById('practice-setup-card').classList.add('hidden');
    document.getElementById('quiz-active-container').classList.remove('hidden');
    
    renderQuizQuestion();
}

function startMockExamOfSize(size) {
    if (state.questionsData.length === 0) {
        showToast('Môn học này chưa có bộ câu hỏi thi thử!', 'danger');
        return;
    }
    
    const qty = Math.min(size, state.questionsData.length);
    let selectedQuestions = [];
    
    const topicsMap = {};
    state.questionsData.forEach(q => {
        if (!topicsMap[q.topicId]) topicsMap[q.topicId] = [];
        topicsMap[q.topicId].push(q);
    });
    
    const topicIds = Object.keys(topicsMap);
    topicIds.forEach(tId => {
        topicsMap[tId] = shuffleArray([...topicsMap[tId]]);
    });
    
    let added = true;
    const topicPointers = {};
    topicIds.forEach(tId => topicPointers[tId] = 0);
    
    while (selectedQuestions.length < qty && added) {
        added = false;
        const shuffledTopicIds = shuffleArray([...topicIds]);
        for (const tId of shuffledTopicIds) {
            const index = topicPointers[tId];
            if (index < topicsMap[tId].length) {
                selectedQuestions.push(topicsMap[tId][index]);
                topicPointers[tId]++;
                added = true;
                if (selectedQuestions.length === qty) break;
            }
        }
    }
    
    selectedQuestions = shuffleArray(selectedQuestions);
    
    const timers = { 20: 25*60, 30: 40*60, 50: 60*60, 100: 120*60 };
    const durationSeconds = timers[size] || 30*60;
    
    state.mock.questions = selectedQuestions;
    state.mock.active = true;
    state.mock.currentIndex = 0;
    state.mock.userAnswers = {};
    state.mock.startTime = new Date();
    state.mock.timer = durationSeconds;
    state.mock.totalTime = durationSeconds;
    
    window.location.hash = '#mock-test';
    document.getElementById('mock-setup-card').classList.add('hidden');
    document.getElementById('mock-exam-workspace-container').classList.remove('hidden');
    
    renderMockQuestionsList();
    startMockTimer();
    renderMockQuestionMap();
}

// Expose dashboard functions globally
window.startPracticeForTopic = startPracticeForTopic;
window.startMockExamOfSize = startMockExamOfSize;

async function renderSubjectDashboard() {
    const container = document.getElementById('subject-dashboard-container');
    if (!container) return;
    
    if (!state.currentSubject) {
        container.innerHTML = '';
        container.classList.add('hidden');
        return;
    }
    
    container.classList.remove('hidden');
    
    const subject = state.currentSubject;
    const subjectId = subject.id;
    const pdfs = subject.pdfs || [];
    
    // Load scanned Markdown exams containing "de"
    const mdExams = await scanSubjectExams(subjectId);
    
    let examsListHTML = '';
    if (mdExams.length > 0) {
        examsListHTML = `
            <div class="dashboard-section" style="margin-top: 16px;">
                <h4 style="font-size: 14px; color: var(--text-muted); margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Đề thi ôn tập (Markdown)</h4>
                <div class="subject-dashboard-chapters-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; margin-bottom: 24px;">
                    ${mdExams.map(filename => {
                        const displayName = filename.replace('.md', '').replace('cauhoi-', '').replace('-attt', '').toUpperCase();
                        return `
                            <button class="btn btn-outline dashboard-chapter-btn" onclick="startMarkdownExam('${filename}')" style="text-align: left; justify-content: flex-start; padding: 14px 18px; font-size: 15px; font-weight: 600; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                                <span class="material-icons-round" style="margin-right: 8px; color: var(--primary); flex-shrink: 0;">quiz</span>
                                <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Đề thi: ${displayName}</span>
                            </button>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }
    
    let presetExamsHTML = '';
    if (state.presetExams && state.presetExams.length > 0) {
        presetExamsHTML = `
            <div class="dashboard-section" style="margin-top: 16px;">
                <h4 style="font-size: 14px; color: var(--text-muted); margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Đề thi mẫu cố định</h4>
                <div class="subject-dashboard-chapters-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; margin-bottom: 24px;">
                    ${state.presetExams.map(exam => {
                        return `
                            <button class="btn btn-outline dashboard-chapter-btn" onclick="startPresetExam('${exam.id}')" style="text-align: left; justify-content: flex-start; padding: 14px 18px; font-size: 15px; font-weight: 600; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                                <span class="material-icons-round" style="margin-right: 8px; color: var(--secondary); flex-shrink: 0;">assignment</span>
                                <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${exam.name}</span>
                            </button>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }
    
    let randomExamHTML = '';
    if (mdExams.length === 0) {
        randomExamHTML = `
            <div class="dashboard-section" style="margin-top: 24px; border-top: 1px solid var(--border-color); padding-top: 20px;">
                <h4 style="font-size: 14px; color: var(--text-muted); margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Thi thử tổng hợp</h4>
                <div style="display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px;">
                    <button class="btn btn-primary" onclick="startMockExamOfSize(50)" style="flex: 1; min-width: 200px; padding: 16px 20px; font-size: 16px; font-weight: 700; display: flex; align-items: center; justify-content: center; gap: 8px;">
                        <span class="material-icons-round">shuffle</span> Tạo đề ngẫu nhiên (50 câu)
                    </button>
                </div>
            </div>
        `;
    } else {
        randomExamHTML = `
            <div class="dashboard-section" style="margin-top: 24px; border-top: 1px solid var(--border-color); padding-top: 20px;">
                <h4 style="font-size: 14px; color: var(--text-muted); margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Thi thử ngẫu nhiên</h4>
                <div style="display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px;">
                    <button class="btn btn-outline" onclick="startMockExamOfSize(50)" style="padding: 12px 20px; font-size: 15px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                        <span class="material-icons-round">shuffle</span> Tạo đề ngẫu nhiên 50 câu
                    </button>
                </div>
            </div>
        `;
    }
    
    const docsHTML = pdfs.length > 0 ? `
        <div class="dashboard-section" style="margin-top: 24px; border-top: 1px solid var(--border-color); padding-top: 20px;">
            <h4 style="font-size: 14px; color: var(--text-muted); margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Tài liệu gốc</h4>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                ${pdfs.map(pdf => {
                    const filename = pdf.split('/').pop();
                    return `
                        <button class="btn btn-outline btn-icon" onclick="window.open('pdf/${pdf}', '_blank')" style="font-size: 14px; font-weight: 600; padding: 10px 16px;">
                            <span class="material-icons-round" style="font-size: 18px;">description</span>
                            Xem tài liệu gốc: ${filename}
                        </button>
                    `;
                }).join('')}
            </div>
        </div>
    ` : '';
    
    const isAI = subject.id === 'trituenhantao-ontap';
    const practicalHTML = isAI ? `
        <div class="dashboard-section" style="margin-top: 24px; border-top: 1px solid var(--border-color); padding-top: 20px;">
            <h4 style="font-size: 14px; color: var(--text-muted); margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Thực hành</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px;">
                <button class="btn btn-outline" onclick="window.location.hash = '#interactive-practice'" style="padding: 14px; font-weight: 600; font-size: 14.5px; display: inline-flex; align-items: center; justify-content: center; gap: 8px;">
                    <span class="material-icons-round">hub</span> AND-OR Search
                </button>
            </div>
        </div>
    ` : '';
    
    container.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 16px;">
                <div style="font-size: 40px; background: rgba(59, 130, 246, 0.1); width: 64px; height: 64px; border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center;">
                    ${subject.icon || '📚'}
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 22px; font-weight: 700; color: var(--text-main);">${subject.name}</h3>
                    <p style="margin: 4px 0 0 0; font-size: 14px; color: var(--text-muted);">${subject.description}</p>
                </div>
            </div>
        </div>
        
        <!-- DANH SÁCH ĐỀ THI -->
        ${examsListHTML}
        ${presetExamsHTML}
        ${randomExamHTML}
        
        <!-- THỰC HÀNH -->
        ${practicalHTML}
        
        <!-- TÀI LIỆU GỐC -->
        ${docsHTML}
    `;
}

function populateMockExamDropdown() {
    const select = document.getElementById('mock-exam-type-select');
    if (!select) return;
    
    // Clear and rebuild options
    select.innerHTML = '<option value="random">Sinh đề ngẫu nhiên từ ngân hàng</option>';
    
    if (state.presetExams && state.presetExams.length > 0) {
        state.presetExams.forEach(exam => {
            const opt = document.createElement('option');
            opt.value = `preset_${exam.id}`;
            opt.textContent = `${exam.name} (${exam.questions.length} câu - 55 phút)`;
            select.appendChild(opt);
        });
    }
    
    // Reset selection to random and show quantity selector
    select.value = 'random';
    const qtyGroup = document.getElementById('mock-qty-selection-group');
    if (qtyGroup) {
        qtyGroup.classList.remove('hidden');
    }
    
    // Sync Custom Select UI
    syncCustomSelect('mock-exam-type-select');
}

// Global Progress Bar Calculator
function updateGlobalProgressBar() {
    const labelPercent = document.getElementById('global-progress-percent');
    const fillBar = document.getElementById('global-progress-bar-fill');
    if (!labelPercent || !fillBar) return;
    
    if (!state.currentSubjectId || state.knowledgeData.length === 0) {
        labelPercent.textContent = '0%';
        fillBar.style.width = '0%';
        return;
    }
    
    const readList = storage.loadReadTopics(state.currentSubjectId);
    const totalTopics = state.knowledgeData.length;
    const readCount = readList.filter(id => state.knowledgeData.some(t => t.topicId === id)).length;
    
    const percent = Math.round((readCount / totalTopics) * 100);
    labelPercent.textContent = `${percent}%`;
    fillBar.style.width = `${percent}%`;
}

// ==========================================================================
// 1. HOME PANEL RENDER
// ==========================================================================

function renderHomeScreen() {
    renderSubjectDashboard();
    
    const container = document.getElementById('subject-cards-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    state.subjects.forEach(subject => {
        const card = document.createElement('div');
        card.className = `subject-card ${subject.id === state.currentSubjectId ? 'active' : ''}`;
        
        const isCurrent = subject.id === state.currentSubjectId;
        const topicCount = isCurrent ? state.knowledgeData.length : 19; 
        const questCount = isCurrent ? state.questionsData.length : 26; 
        
        card.innerHTML = `
            <div class="subject-card-header">
                <div class="subject-icon-box">${subject.icon || '📚'}</div>
                ${isCurrent ? '<span class="badge"><span class="material-icons-round" style="font-size:14px">check</span> Đang chọn</span>' : ''}
            </div>
            <div class="subject-card-body">
                <h4>${subject.name}</h4>
                <p>${subject.description}</p>
            </div>
            <div class="subject-stats">
                <div class="stat-group">
                    <span class="material-icons-round">folder</span>
                    <span>${topicCount} Chủ đề</span>
                </div>
                <div class="stat-group">
                    <span class="material-icons-round">help_outline</span>
                    <span>${questCount} Câu hỏi</span>
                </div>
            </div>
            <div class="subject-card-footer">
                <button class="btn ${isCurrent ? 'btn-primary' : 'btn-outline'} btn-sm">
                    ${isCurrent ? 'Đang kích hoạt' : 'Chọn môn học'}
                </button>
            </div>
        `;
        
        card.addEventListener('click', async () => {
            if (!isCurrent) {
                await selectSubject(subject.id);
            }
            renderHomeScreen();
        });
        
        container.appendChild(card);
    });
}

// ==========================================================================
// 2. KNOWLEDGE PANEL RENDER (Notes + Markdown style presentation)
// ==========================================================================
function renderKnowledgeSidebarItems(query = '') {
    const topicListEl = document.getElementById('knowledge-topic-list');
    if (!topicListEl) return;
    
    topicListEl.innerHTML = '';
    const readList = storage.loadReadTopics(state.currentSubjectId);
    
    const cleanQuery = query.toLowerCase().trim();
    const filteredTopics = state.knowledgeData.filter(topic => {
        return topic.title.toLowerCase().includes(cleanQuery) || 
               (topic.summary && topic.summary.toLowerCase().includes(cleanQuery)) ||
               (topic.keywords && topic.keywords.some(k => k.toLowerCase().includes(cleanQuery)));
    });
    
    if (filteredTopics.length === 0) {
        topicListEl.innerHTML = '<div class="empty-list-info" style="padding: 20px; text-align: center; color: var(--text-muted);">Không tìm thấy chủ đề nào.</div>';
        return;
    }
    
    if (state.knowledgeData.length > 8) {
        const groups = {
            'theory': { name: '📖 Lý thuyết & Khái niệm', items: [] },
            'practical': { name: '🛠️ Thực hành & Mô phỏng', items: [] },
            'exam': { name: '📝 Ngân hàng đề & Ôn tập', items: [] }
        };
        
        filteredTopics.forEach(topic => {
            const title = topic.title.toLowerCase();
            const id = topic.topicId.toLowerCase();
            if (title.includes('ngân hàng') || title.includes('tổng hợp') || title.includes('đề thi') || title.includes('trắc nghiệm') || title.includes('part') || title.includes('phần') || id.includes('other_topics') || id.includes('part')) {
                groups['exam'].items.push(topic);
            } else if (title.includes('thực hành') || title.includes('interactive') || title.includes('vẽ đồ thị') || title.includes('lab') || title.includes('tự luận') || id.includes('interactive')) {
                groups['practical'].items.push(topic);
            } else {
                groups['theory'].items.push(topic);
            }
        });
        
        Object.keys(groups).forEach(gKey => {
            const g = groups[gKey];
            if (g.items.length === 0) return;
            
            const header = document.createElement('div');
            const isCollapsed = cleanQuery ? false : state.knowledgeGroupsCollapsed[gKey]; 
            header.className = `ksb-group-header ${isCollapsed ? 'collapsed' : ''}`;
            header.style.display = 'flex';
            header.style.alignItems = 'center';
            header.style.justifyContent = 'space-between';
            header.style.padding = '10px 16px';
            header.style.background = 'var(--border-color-light)';
            header.style.cursor = 'pointer';
            header.style.fontWeight = '700';
            header.style.fontSize = '13px';
            header.style.color = 'var(--text-muted)';
            header.style.borderBottom = '1px solid var(--border-color)';
            
            header.innerHTML = `
                <span>${g.name} (${g.items.length})</span>
                <span class="material-icons-round" style="font-size: 18px; transition: transform 0.2s; transform: rotate(${isCollapsed ? '-90deg' : '0deg'});">
                    expand_more
                </span>
            `;
            
            header.addEventListener('click', () => {
                state.knowledgeGroupsCollapsed[gKey] = !state.knowledgeGroupsCollapsed[gKey];
                renderKnowledgeSidebarItems(query);
            });
            
            topicListEl.appendChild(header);
            
            if (!isCollapsed) {
                g.items.forEach(topic => {
                    const item = document.createElement('div');
                    const isRead = readList.includes(topic.topicId);
                    const isActive = topic.topicId === state.selectedTopicId;
                    
                    item.className = `ksb-item ${isActive ? 'active' : ''} ${isRead ? 'read' : ''}`;
                    item.innerHTML = `
                        <span class="material-icons-round ksb-status-icon">
                            ${isRead ? 'check_circle' : 'radio_button_unchecked'}
                        </span>
                        <span class="ksb-title" title="${topic.title}">${topic.title}</span>
                    `;
                    
                    item.addEventListener('click', () => {
                        state.selectedTopicId = topic.topicId;
                        const searchInput = document.getElementById('ksb-search-input');
                        const currentQuery = searchInput ? searchInput.value : '';
                        renderKnowledgeScreen(currentQuery);
                    });
                    
                    topicListEl.appendChild(item);
                });
            }
        });
    } else {
        filteredTopics.forEach(topic => {
            const item = document.createElement('div');
            const isRead = readList.includes(topic.topicId);
            const isActive = topic.topicId === state.selectedTopicId;
            
            item.className = `ksb-item ${isActive ? 'active' : ''} ${isRead ? 'read' : ''}`;
            item.innerHTML = `
                <span class="material-icons-round ksb-status-icon">
                    ${isRead ? 'check_circle' : 'radio_button_unchecked'}
                </span>
                <span class="ksb-title" title="${topic.title}">${topic.title}</span>
            `;
            
            item.addEventListener('click', () => {
                state.selectedTopicId = topic.topicId;
                renderKnowledgeScreen();
            });
            
            topicListEl.appendChild(item);
        });
    }
}

function renderKnowledgeScreen(initialQuery = '') {
    const topicListEl = document.getElementById('knowledge-topic-list');
    const detailViewEl = document.getElementById('knowledge-detail-view');
    if (!topicListEl || !detailViewEl) return;
    
    topicListEl.innerHTML = '';
    
    if (state.knowledgeData.length === 0) {
        topicListEl.innerHTML = '<div class="empty-list-info">Không có chủ đề nào.</div>';
        detailViewEl.innerHTML = '<div class="empty-state"><h3>Không có dữ liệu</h3></div>';
        return;
    }
    
    if (!state.knowledgeGroupsCollapsed) {
        state.knowledgeGroupsCollapsed = {
            'theory': false,
            'practical': false,
            'exam': false
        };
    }
    
    let searchBox = document.getElementById('ksb-search-container');
    if (state.knowledgeData.length > 8) {
        if (!searchBox) {
            searchBox = document.createElement('div');
            searchBox.id = 'ksb-search-container';
            searchBox.className = 'ksb-search-box';
            searchBox.style.padding = '12px 16px';
            searchBox.style.borderBottom = '1px solid var(--border-color)';
            searchBox.innerHTML = `
                <div style="position: relative;">
                    <input type="text" id="ksb-search-input" value="${initialQuery}" placeholder="Tìm kiếm chương/bài..." style="width: 100%; padding: 8px 12px 8px 36px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); background: var(--bg-app); color: var(--text-main); font-size: 13.5px;">
                    <span class="material-icons-round" style="position: absolute; left: 10px; top: 9px; font-size: 18px; color: var(--text-muted);">search</span>
                </div>
            `;
            topicListEl.parentNode.insertBefore(searchBox, topicListEl);
            
            const searchInput = document.getElementById('ksb-search-input');
            searchInput.addEventListener('input', () => {
                renderKnowledgeSidebarItems(searchInput.value);
            });
        } else {
            const searchInput = document.getElementById('ksb-search-input');
            if (searchInput && initialQuery) {
                searchInput.value = initialQuery;
            }
        }
    } else {
        if (searchBox) searchBox.remove();
    }
    
    const searchInput = document.getElementById('ksb-search-input');
    const currentQuery = searchInput ? searchInput.value : initialQuery;
    renderKnowledgeSidebarItems(currentQuery);
    
    // Render active topic details
    const activeTopic = state.knowledgeData.find(t => t.topicId === state.selectedTopicId);
    if (!activeTopic) {
        detailViewEl.innerHTML = `
            <div class="empty-state">
                <span class="material-icons-round large-icon">menu_book</span>
                <h3>Vui lòng chọn một chủ đề</h3>
                <p>Chọn chủ đề ở thanh danh sách bên trái để bắt đầu học.</p>
            </div>
        `;
        return;
    }
    
    const isTopicRead = readList.includes(activeTopic.topicId);
    const personalNote = localStorage.getItem(storage.getNoteKey(state.currentSubjectId, activeTopic.topicId)) || '';
    
    const pdfs = state.currentSubject.pdfs || [];
    const docButtonsHTML = pdfs.length > 0 ? `
        <div class="detail-doc-links" style="display: flex; gap: 8px; margin-top: 8px; flex-wrap: wrap;">
            ${pdfs.map(pdf => {
                const filename = pdf.split('/').pop();
                return `
                    <button class="btn btn-outline btn-xs" onclick="window.open('pdf/${pdf}', '_blank')" style="padding: 6px 12px; font-size: 12.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
                        <span class="material-icons-round" style="font-size: 15px;">description</span>
                        Xem đầy đủ: ${filename}
                    </button>
                `;
            }).join('')}
        </div>
    ` : '';
    
    detailViewEl.innerHTML = `
        <div class="detail-header">
            <div class="topic-label-wrap">
                <span class="badge">Chủ đề học tập</span>
                <h2 class="detail-title">${activeTopic.title}</h2>
                ${docButtonsHTML}
            </div>
            <button class="btn btn-mark-read ${isTopicRead ? 'read' : ''}" id="btn-toggle-read">
                <span class="material-icons-round">${isTopicRead ? 'check' : 'bookmark_border'}</span>
                <span>${isTopicRead ? 'Đã học' : 'Đánh dấu đã học'}</span>
            </button>
        </div>
        
        <div class="content-section">
            <h4><span class="material-icons-round text-primary" style="font-size: 20px">article</span> Tóm tắt lý thuyết:</h4>
            <div class="content-text">${activeTopic.content}</div>
        </div>
        
        ${activeTopic.example ? `
        <div class="content-section">
            <h4><span class="material-icons-round text-primary" style="font-size: 20px">code</span> Ví dụ minh họa:</h4>
            <div class="code-box-wrapper">
                <div class="code-box-header">
                    <span class="code-lang">Java / Code Block</span>
                    <button class="btn-copy-code" id="btn-copy-code-snippet">
                        <span class="material-icons-round">content_copy</span> Sao chép
                    </button>
                </div>
                <pre><code id="code-snippet-element">${escapeHTML(activeTopic.example)}</code></pre>
            </div>
        </div>
        ` : ''}
        
        <!-- Note Section -->
        <div class="content-section note-area-card">
            <div class="note-header">
                <h4><span class="material-icons-round">edit</span> Ghi chú cá nhân:</h4>
                <span class="badge" style="background:#fef3c7; color:#d97706" id="note-save-status">Đã lưu tự động vào LocalStorage</span>
            </div>
            <textarea class="note-input" id="topic-notes-textarea" placeholder="Nhập ghi chú cá nhân của bạn tại đây (ví dụ: mẹo nhớ, công thức, phần quan trọng cần lưu ý...)">${personalNote}</textarea>
            <div class="note-actions">
                <button class="btn btn-secondary btn-sm" id="btn-save-notes">Lưu ghi chú</button>
            </div>
        </div>
        
        <!-- Navigation Footer -->
        <div class="detail-footer">
            <button class="btn btn-outline" id="btn-prev-topic" ${isFirstTopic() ? 'disabled' : ''}>
                <span class="material-icons-round">arrow_back</span> Chủ đề trước
            </button>
            <button class="btn btn-secondary" id="btn-practice-this-topic">
                <span class="material-icons-round">psychology</span> Ôn tập chủ đề này
            </button>
            <button class="btn btn-outline" id="btn-next-topic" ${isLastTopic() ? 'disabled' : ''}>
                Chủ đề tiếp theo <span class="material-icons-round">arrow_forward</span>
            </button>
        </div>
    `;
    
    // Attach detail panel actions
    document.getElementById('btn-toggle-read').addEventListener('click', toggleReadStatus);
    
    if (activeTopic.example) {
        document.getElementById('btn-copy-code-snippet').addEventListener('click', copyCodeSnippet);
    }
    
    // Setup note autosave & click save
    const noteArea = document.getElementById('topic-notes-textarea');
    document.getElementById('btn-save-notes').addEventListener('click', () => {
        savePersonalNotes(noteArea.value);
        showToast('Đã lưu ghi chú cá nhân!', 'success');
    });
    
    // Auto save note when user stops typing (debounce)
    let autoSaveTimeout;
    noteArea.addEventListener('input', () => {
        const statusEl = document.getElementById('note-save-status');
        if (statusEl) statusEl.textContent = 'Đang nhập...';
        
        clearTimeout(autoSaveTimeout);
        autoSaveTimeout = setTimeout(() => {
            savePersonalNotes(noteArea.value);
            if (statusEl) statusEl.textContent = 'Đã tự động lưu';
        }, 1500);
    });
    
    // Navigation triggers
    document.getElementById('btn-prev-topic').addEventListener('click', () => navigateTopic(-1));
    document.getElementById('btn-next-topic').addEventListener('click', () => navigateTopic(1));
    
    document.getElementById('btn-practice-this-topic').addEventListener('click', () => {
        // Force navigate to practice, selecting ONLY this topic
        state.quiz.selectedTopics = [activeTopic.topicId];
        window.location.hash = '#practice';
        // Auto trigger quiz starting
        setTimeout(() => {
            startPracticeQuizDirectly();
        }, 100);
    });
}

function escapeHTML(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}

function highlightPython(code) {
    const placeholders = [];
    let text = code;
    
    // Mask strings: &quot;...&quot;, &#039;...&#039;, "...", '...'
    text = text.replace(/(&quot;[\s\S]*?&quot;|&#039;[\s\S]*?&#039;|"[\s\S]*?"|'[\s\S]*?')/g, function(match) {
        placeholders.push(`<span class="code-string">${match}</span>`);
        return `__TOKEN_PLACEHOLDER_${placeholders.length - 1}__`;
    });
    
    // Mask comments: # ...
    text = text.replace(/(#[^\n]*)/g, function(match) {
        placeholders.push(`<span class="code-comment">${match}</span>`);
        return `__TOKEN_PLACEHOLDER_${placeholders.length - 1}__`;
    });
    
    // Highlight keywords
    const keywords = ['def', 'class', 'import', 'return', 'if', 'else', 'elif', 'for', 'in', 'while', 'try', 'except', 'as', 'lambda', 'and', 'or', 'not', 'break', 'continue', 'pass', 'global', 'from', 'with'];
    keywords.forEach(kw => {
        const regex = new RegExp(`\\b(${kw})\\b`, 'g');
        text = text.replace(regex, '<span class="code-keyword">$1</span>');
    });
    
    // Highlight builtins
    const builtins = ['print', 'len', 'type', 'int', 'float', 'str', 'list', 'dict', 'set', 'tuple', 'range', 'super', 'sum', 'sorted'];
    builtins.forEach(bi => {
        const regex = new RegExp(`\\b(${bi})\\b`, 'g');
        text = text.replace(regex, '<span class="code-builtin">$1</span>');
    });
    
    // Highlight constants
    const constants = ['True', 'False', 'None'];
    constants.forEach(c => {
        const regex = new RegExp(`\\b(${c})\\b`, 'g');
        text = text.replace(regex, '<span class="code-constant">$1</span>');
    });
    
    // Restore strings and comments
    text = text.replace(/__TOKEN_PLACEHOLDER_(\d+)__/g, function(match, p1) {
        return placeholders[parseInt(p1)];
    });
    
    return text;
}

function cleanVietnameseText(str) {
    if (str === undefined || str === null) {
        return 'Chưa có dữ liệu';
    }
    if (typeof str !== 'string') {
        return str;
    }
    
    const trimmed = str.trim();
    if (trimmed === 'undefined' || trimmed === 'null' || trimmed === 'NaN' || trimmed === '[object Object]') {
        return 'Chưa có dữ liệu';
    }
    
    let text = trimmed.normalize('NFC');
    
    // Fix split consonant clusters: c h -> ch, p h -> ph, etc.
    text = text.replace(/\b(c|p|t|g|k|n|q) +(h|r|i|g|u)(?=[a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ\s]+)/gi, '$1$2');
    
    // Fix split words starting with a consonant, followed by space, then a tone-marked vowel
    const consonants = 'b|c|ch|d|đ|g|gh|gi|h|k|kh|l|m|n|nh|ng|ngh|p|ph|qu|r|s|t|th|tr|v|x';
    const toneMarkedVowels = 'áàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ';
    const allVowelsAndChars = 'a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ';
    
    const initialConsonantRegex = new RegExp(`\\b(${consonants}) +([${toneMarkedVowels}][${allVowelsAndChars}]*)\\b`, 'gi');
    text = text.replace(initialConsonantRegex, '$1$2');
    
    // Fix split diphthongs / triphthongs
    // 1. i + space + [êếềểễệ] -> iê...
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*i) +([êếềểễệ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    // 2. u + space + [ôốồổỗộ] -> uô...
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*u) +([ôốồổỗộ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    // 3. ư + space + [ơớờởỡợ] -> ươ...
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*ư) +([ơớờởỡợ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    // 4. o + space + [aáàảãạeéèẻẽẹ] -> oa / oe
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*o) +([aáàảãạeéèẻẽẹ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    // 5. u + space + [âấầẩẫậêếềểễệaáàảãạ] -> uâ / uê / ua
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*u) +([âấầẩẫậêếềểễệaáàảãạ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    // 6. u + space + [yýỳỷỹỵ] -> uy
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*u) +([yýỳỷỹỵ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    // 7. y + space + [êếềểễệ] -> yê
    text = text.replace(/\b([bBcCdDđĐgGhHkKlLmMnNpPqQrRsStTvVxX]*y) +([êếềểễệ][a-zA-ZĂăÂâĐđÊêÔôƠơƯưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]*)\b/gi, '$1$2');
    
    // Specific split words cleanups
    text = text.replace(/\bth +am\b/gi, 'tham');
    text = text.replace(/\bph +ương\b/gi, 'phương');
    
    // Clean up duplicate spaces inside words, but keep single spaces
    text = text.replace(/ +/g, ' ');
    
    return text;
}

function cleanObjectText(obj) {
    if (obj === null || obj === undefined) return obj;
    if (typeof obj === 'string') {
        return cleanVietnameseText(obj);
    }
    if (Array.isArray(obj)) {
        return obj.map(item => cleanObjectText(item));
    }
    if (typeof obj === 'object') {
        const cleaned = {};
        for (const key in obj) {
            if (Object.prototype.hasOwnProperty.call(obj, key)) {
                cleaned[key] = cleanObjectText(obj[key]);
            }
        }
        return cleaned;
    }
    return obj;
}

function formatMarkdown(str) {
    if (!str) return '';
    let html = escapeHTML(str);
    
    // Convert code blocks: ```python ... ``` (supports CRLF)
    html = html.replace(/```(?:python|javascript|java|)\r?\n([\s\S]*?)```/g, function(match, p1) {
        const highlighted = highlightPython(p1);
        return `<div class="code-box-wrapper"><pre><code>${highlighted}</code></pre></div>`;
    });
    
    // Convert inline code: `code`
    html = html.replace(/`([^`\n]+)`/g, '<code>$1</code>');
    
    // Temporarily extract code-box-wrapper blocks to prevent replacing \n with <br> inside them
    const blocks = [];
    html = html.replace(/<div class="code-box-wrapper">[\s\S]*?<\/div>/g, function(match) {
        blocks.push(match);
        return `__CODE_BLOCK_${blocks.length - 1}__`;
    });
    
    // Replace newlines with <br> in normal text (supports CRLF)
    html = html.replace(/\r?\n/g, '<br>');
    
    // Restore blocks
    html = html.replace(/__CODE_BLOCK_(\d+)__/g, function(match, p1) {
        return blocks[parseInt(p1)];
    });
    
    return html;
}

function isFirstTopic() {
    const idx = state.knowledgeData.findIndex(t => t.topicId === state.selectedTopicId);
    return idx === 0;
}

function isLastTopic() {
    const idx = state.knowledgeData.findIndex(t => t.topicId === state.selectedTopicId);
    return idx === state.knowledgeData.length - 1;
}

function navigateTopic(direction) {
    const idx = state.knowledgeData.findIndex(t => t.topicId === state.selectedTopicId);
    const targetIdx = idx + direction;
    if (targetIdx >= 0 && targetIdx < state.knowledgeData.length) {
        state.selectedTopicId = state.knowledgeData[targetIdx].topicId;
        renderKnowledgeScreen();
    }
}

function toggleReadStatus() {
    if (!state.currentSubjectId || !state.selectedTopicId) return;
    
    let readList = storage.loadReadTopics(state.currentSubjectId);
    const idx = readList.indexOf(state.selectedTopicId);
    
    if (idx > -1) {
        readList.splice(idx, 1);
        showToast('Đã bỏ đánh dấu đã đọc', 'info');
    } else {
        readList.push(state.selectedTopicId);
        showToast('Tuyệt vời! Đã hoàn thành chủ đề.', 'success');
    }
    
    storage.saveReadTopics(state.currentSubjectId, readList);
    updateGlobalProgressBar();
    renderKnowledgeScreen(); // Refresh UI list icons
}

function copyCodeSnippet() {
    const codeEl = document.getElementById('code-snippet-element');
    if (!codeEl) return;
    
    navigator.clipboard.writeText(codeEl.textContent)
        .then(() => {
            showToast('Đã sao chép code ví dụ!', 'success');
        })
        .catch(err => {
            console.error('Không thể copy code:', err);
        });
}

function savePersonalNotes(text) {
    if (!state.currentSubjectId || !state.selectedTopicId) return;
    localStorage.setItem(
        storage.getNoteKey(state.currentSubjectId, state.selectedTopicId),
        text
    );
}

// ==========================================================================
// 3. PRACTICE PANEL (Topic Quiz Lifecycle)
// ==========================================================================
function renderPracticeSetupScreen() {
    const checkboxContainer = document.getElementById('practice-topics-checkbox-container');
    if (!checkboxContainer) return;
    
    checkboxContainer.innerHTML = '';
    
    if (state.knowledgeData.length === 0) {
        checkboxContainer.innerHTML = '<p>Không có dữ liệu chủ đề.</p>';
        return;
    }
    
    state.knowledgeData.forEach(topic => {
        const isChecked = state.quiz.selectedTopics.includes(topic.topicId);
        const label = document.createElement('label');
        label.className = `topic-checkbox-label ${isChecked ? 'checked' : ''}`;
        
        label.innerHTML = `
            <input type="checkbox" value="${topic.topicId}" ${isChecked ? 'checked' : ''}>
            <span>${topic.title}</span>
        `;
        
        // Listen directly for styles updates
        const input = label.querySelector('input');
        input.addEventListener('change', (e) => {
            const val = e.target.value;
            if (e.target.checked) {
                label.classList.add('checked');
                if (!state.quiz.selectedTopics.includes(val)) {
                    state.quiz.selectedTopics.push(val);
                }
            } else {
                label.classList.remove('checked');
                state.quiz.selectedTopics = state.quiz.selectedTopics.filter(id => id !== val);
            }
        });
        
        checkboxContainer.appendChild(label);
    });
}

function toggleAllTopicCheckboxes(checked) {
    const checkboxes = document.querySelectorAll('#practice-topics-checkbox-container input[type="checkbox"]');
    state.quiz.selectedTopics = [];
    
    checkboxes.forEach(cb => {
        cb.checked = checked;
        const parent = cb.closest('.topic-checkbox-label');
        if (checked) {
            parent.classList.add('checked');
            state.quiz.selectedTopics.push(cb.value);
        } else {
            parent.classList.remove('checked');
        }
    });
}

// Function called when user redirects from a specific topic using "Practice this topic"
function startPracticeQuizDirectly() {
    renderPracticeSetupScreen();
    startPracticeQuiz();
}

function startPracticeQuiz() {
    if (state.quiz.selectedTopics.length === 0) {
        showToast('Vui lòng chọn ít nhất một chủ đề để ôn tập!', 'warning');
        return;
    }
    
    // Filter questions matching selected topics
    let questions = state.questionsData.filter(q => state.quiz.selectedTopics.includes(q.topicId));
    
    if (questions.length === 0) {
        showToast('Không tìm thấy câu hỏi nào thuộc chủ đề đã chọn!', 'danger');
        return;
    }
    
    // Shuffle filtered questions
    state.quiz.questions = shuffleArray([...questions]);
    state.quiz.active = true;
    state.quiz.currentIndex = 0;
    state.quiz.score = 0;
    state.quiz.userAnswers = [];
    state.quiz.checked = false;
    
    // Hide Setup View, Reveal Quiz View
    document.getElementById('practice-setup-card').classList.add('hidden');
    document.getElementById('quiz-active-container').classList.remove('hidden');
    
    renderQuizQuestion();
}

function renderQuizQuestion() {
    const q = state.quiz.questions[state.quiz.currentIndex];
    
    // Set question header details
    document.getElementById('quiz-current-index').textContent = state.quiz.currentIndex + 1;
    document.getElementById('quiz-total-count').textContent = state.quiz.questions.length;
    
    // Find topic title
    const topic = state.knowledgeData.find(t => t.topicId === q.topicId);
    document.getElementById('quiz-current-topic-tag').textContent = topic ? topic.title : 'Tổng hợp';
    
    // Progress fill
    const progressPercent = ((state.quiz.currentIndex) / state.quiz.questions.length) * 100;
    document.getElementById('quiz-progress-bar-fill').style.width = `${progressPercent}%`;
    
    // Render question text
    document.getElementById('quiz-question-text').innerHTML = formatMarkdown(q.question);
    
    // Render options cards
    const optionsContainer = document.getElementById('quiz-options-container');
    optionsContainer.innerHTML = '';
    
    q.options.forEach((opt, idx) => {
        const letter = String.fromCharCode(65 + idx);
        const card = document.createElement('div');
        card.className = 'option-card';
        card.dataset.index = idx;
        card.dataset.letter = letter;
        
        card.innerHTML = `
            <div class="option-badge">${letter}</div>
            <div class="option-text">${opt}</div>
        `;
        
        card.addEventListener('click', () => selectQuizOption(card));
        optionsContainer.appendChild(card);
    });
    
    // Hide explanation box and disable next button initially
    document.getElementById('quiz-explanation-box').classList.add('hidden');
    
    const nextBtn = document.getElementById('btn-next-question');
    nextBtn.disabled = true;
    nextBtn.innerHTML = `Kiểm tra đáp án <span class="material-icons-round">task_alt</span>`;
    state.quiz.checked = false;
}

function selectQuizOption(selectedCard) {
    if (state.quiz.checked) return; // Prevent changing selection after check
    
    const allOptions = document.querySelectorAll('#quiz-options-container .option-card');
    allOptions.forEach(card => card.classList.remove('selected'));
    
    selectedCard.classList.add('selected');
    
    // Enable Next button (which acts as Check)
    const nextBtn = document.getElementById('btn-next-question');
    nextBtn.disabled = false;
}

function handleNextQuizQuestion() {
    const nextBtn = document.getElementById('btn-next-question');
    
    if (!state.quiz.checked) {
        // STATE 1: CHECKING ANSWER
        const selectedOpt = document.querySelector('#quiz-options-container .option-card.selected');
        if (!selectedOpt) return;
        
        const chosenLetter = selectedOpt.dataset.letter; // 'A', 'B', 'C', 'D'
        const currentQuestion = state.quiz.questions[state.quiz.currentIndex];
        const correctLetter = currentQuestion.correctAnswer;
        
        state.quiz.userAnswers.push(chosenLetter);
        
        // Show correct / wrong feedbacks
        const allCards = document.querySelectorAll('#quiz-options-container .option-card');
        allCards.forEach(card => {
            card.classList.add('disabled');
            if (card.dataset.letter === correctLetter) {
                card.classList.add('correct');
            } else if (card.dataset.letter === chosenLetter) {
                card.classList.add('incorrect');
            }
        });
        
        const isCorrect = chosenLetter === correctLetter;
        if (isCorrect) {
            state.quiz.score++;
        }
        
        // Update analytics statistics in LocalStorage
        updateAnswerStatistics(currentQuestion.topicId, isCorrect);
        
        // Show explanation
        const explanationBox = document.getElementById('quiz-explanation-box');
        const explanationText = document.getElementById('quiz-explanation-text');
        
        if (explanationText && currentQuestion.explanation) {
            explanationText.innerHTML = formatMarkdown(currentQuestion.explanation);
            explanationBox.classList.remove('hidden');
        }
        
        // Configure Next Button
        state.quiz.checked = true;
        
        const isLast = state.quiz.currentIndex === state.quiz.questions.length - 1;
        if (isLast) {
            nextBtn.innerHTML = `Hoàn thành <span class="material-icons-round">emoji_events</span>`;
        } else {
            nextBtn.innerHTML = `Tiếp tục <span class="material-icons-round">arrow_forward</span>`;
        }
    } else {
        // STATE 2: NAVIGATING TO NEXT OR RESULTS
        const isLast = state.quiz.currentIndex === state.quiz.questions.length - 1;
        if (isLast) {
            showPracticeQuizResults();
        } else {
            state.quiz.currentIndex++;
            renderQuizQuestion();
        }
    }
}

function quitPracticeQuiz() {
    state.quiz.active = false;
    document.getElementById('quiz-active-container').classList.add('hidden');
    document.getElementById('practice-setup-card').classList.remove('hidden');
    // Clear selections
    state.quiz.selectedTopics = [];
    renderPracticeSetupScreen();
}

function showPracticeQuizResults() {
    state.quiz.active = false;
    document.getElementById('quiz-active-container').classList.add('hidden');
    
    // Increment total quizzes taken
    const stats = storage.loadStats(state.currentSubjectId);
    stats.quizzesTaken++;
    storage.saveStats(state.currentSubjectId, stats);
    
    const accuracy = Math.round((state.quiz.score / state.quiz.questions.length) * 100);
    renderResultsPanel(state.quiz.score, state.quiz.questions.length, accuracy, null, state.quiz.questions, state.quiz.userAnswers);
}

// Statistics recording functions
function updateAnswerStatistics(topicId, isCorrect) {
    if (!state.currentSubjectId) return;
    const stats = storage.loadStats(state.currentSubjectId);
    
    if (!stats.topicStats[topicId]) {
        stats.topicStats[topicId] = { correct: 0, total: 0 };
    }
    
    stats.topicStats[topicId].total++;
    if (isCorrect) {
        stats.topicStats[topicId].correct++;
    }
    
    storage.saveStats(state.currentSubjectId, stats);
}

// ==========================================================================
// 4. MOCK TEST PANEL (Simulation with timer + grid map nav)
// ==========================================================================
function startMockExam() {
    const select = document.getElementById('mock-exam-type-select');
    const examType = select ? select.value : 'random';
    
    let selectedQuestions = [];
    let durationSeconds = 30 * 60;
    let questionQty = 50;
    
    if (examType === 'random') {
        const qtyRadio = document.querySelector('input[name="mock-qty"]:checked');
        questionQty = qtyRadio ? parseInt(qtyRadio.value) : 20;
        
        if (state.questionsData.length === 0) {
            showToast('Môn học này chưa có bộ câu hỏi thi thử!', 'danger');
            return;
        }
        
        // Choose N questions with balanced distribution over topics
        const qty = Math.min(questionQty, state.questionsData.length);
        
        // Group questions by topicId
        const topicsMap = {};
        state.questionsData.forEach(q => {
            if (!topicsMap[q.topicId]) topicsMap[q.topicId] = [];
            topicsMap[q.topicId].push(q);
        });
        
        // Shuffle each group
        const topicIds = Object.keys(topicsMap);
        topicIds.forEach(tId => {
            topicsMap[tId] = shuffleArray([...topicsMap[tId]]);
        });
        
        // Select questions round-robin to ensure balance
        let added = true;
        const topicPointers = {};
        topicIds.forEach(tId => topicPointers[tId] = 0);
        
        while (selectedQuestions.length < qty && added) {
            added = false;
            // Shuffle topic list order in each round to prevent biases
            const shuffledTopicIds = shuffleArray([...topicIds]);
            for (const tId of shuffledTopicIds) {
                const index = topicPointers[tId];
                if (index < topicsMap[tId].length) {
                    selectedQuestions.push(topicsMap[tId][index]);
                    topicPointers[tId]++;
                    added = true;
                    if (selectedQuestions.length === qty) break;
                }
            }
        }
        
        // Shuffle the final list so questions from the same topic are not grouped together
        selectedQuestions = shuffleArray(selectedQuestions);
        
        // Determine exam time (in seconds)
        const timers = { 20: 25*60, 30: 40*60, 50: 60*60, 100: 120*60 };
        durationSeconds = timers[questionQty] || 30*60;
    } else {
        // Load preset exam
        const examId = examType.replace('preset_', '');
        const preset = state.presetExams.find(e => e.id === examId);
        if (!preset) {
            showToast('Không tìm thấy đề thi mẫu!', 'danger');
            return;
        }
        
        selectedQuestions = [...preset.questions];
        questionQty = selectedQuestions.length;
        durationSeconds = 55 * 60; // 55 minutes = 3300 seconds
    }
    
    state.mock.questions = selectedQuestions;
    state.mock.active = true;
    state.mock.currentIndex = 0;
    state.mock.userAnswers = {};
    state.mock.startTime = new Date();
    
    state.mock.timer = durationSeconds;
    state.mock.totalTime = durationSeconds;
    
    // Hide configurator, reveal exam workspace
    document.getElementById('mock-setup-card').classList.add('hidden');
    document.getElementById('mock-exam-workspace-container').classList.remove('hidden');
    
    // Start countdown
    startMockTimer();
    
    // Build Navigation Question Map Grid
    renderMockQuestionMap();
    
    // Display first question
    renderMockQuestion();
}

function startMockTimer() {
    clearMockTimer();
    
    const updateDisplay = () => {
        const display = document.getElementById('mock-timer-text');
        if (!display) return;
        
        const mins = Math.floor(state.mock.timer / 60);
        const secs = state.mock.timer % 60;
        display.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        
        // Add danger blink on low time (under 1 minute)
        const timerContainer = document.getElementById('mock-timer');
        if (timerContainer) {
            if (state.mock.timer <= 60) {
                timerContainer.style.background = '#fee2e2';
                timerContainer.style.color = '#ef4444';
            } else {
                timerContainer.style.background = '';
                timerContainer.style.color = '';
            }
        }
    };
    
    updateDisplay();
    
    state.mock.timerInterval = setInterval(() => {
        state.mock.timer--;
        updateDisplay();
        
        if (state.mock.timer <= 0) {
            clearMockTimer();
            showToast('Hết thời gian làm bài! Hệ thống tự động nộp bài.', 'warning');
            submitMockExam(true);
        }
    }, 1000);
}

function clearMockTimer() {
    if (state.mock.timerInterval) {
        clearInterval(state.mock.timerInterval);
        state.mock.timerInterval = null;
    }
}

function renderMockQuestionMap() {
    const mapContainer = document.getElementById('mock-question-map');
    if (!mapContainer) return;
    
    mapContainer.innerHTML = '';
    
    state.mock.questions.forEach((_, idx) => {
        const btn = document.createElement('button');
        btn.className = 'map-btn';
        btn.id = `mock-map-btn-${idx}`;
        btn.textContent = idx + 1;
        
        btn.addEventListener('click', () => {
            jumpToMockQuestion(idx);
        });
        
        mapContainer.appendChild(btn);
    });
    
    updateMockQuestionMapStatus();
}

function updateMockQuestionMapStatus() {
    state.mock.questions.forEach((_, idx) => {
        const btn = document.getElementById(`mock-map-btn-${idx}`);
        if (!btn) return;
        
        // Remove old indicators
        btn.classList.remove('current', 'answered');
        
        // Apply status class
        if (idx === state.mock.currentIndex) {
            btn.classList.add('current');
        } else if (state.mock.userAnswers[idx] !== undefined) {
            btn.classList.add('answered');
        }
    });
}

function renderMockQuestionsList() {
    const pane = document.querySelector('.mock-question-pane');
    if (!pane) return;
    
    pane.innerHTML = `
        <div class="mock-header-sticky" style="position: sticky; top: 0; background: var(--bg-card); padding: 16px 24px; border-bottom: 2px solid var(--border-color); z-index: 100; display: flex; justify-content: space-between; align-items: center; border-radius: var(--radius-md) var(--radius-md) 0 0; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <h4 style="margin: 0; font-weight: 700; font-size: 18px;">Bài thi thử: ${state.currentSubject.name}</h4>
            <div class="timer-display" id="mock-timer" style="display: flex; align-items: center; gap: 8px; font-family: 'Outfit', sans-serif; font-size: 18px; font-weight: 700; color: var(--danger); padding: 6px 14px; background: rgba(239, 68, 68, 0.1); border-radius: 20px;">
                <span class="material-icons-round">timer</span>
                <span id="mock-timer-text">00:00</span>
            </div>
        </div>
        <div class="mock-questions-scroll-area" style="display: flex; flex-direction: column; gap: 20px;">
            ${state.mock.questions.map((q, idx) => {
                const isMultiSelect = q.multiSelect === true;
                const savedAnswer = state.mock.userAnswers[idx];
                
                const optionBadges = Array.from({length: q.options.length}, (_, i) => String.fromCharCode(65 + i));
                const isLong = q.question.length > 150;
                const qTextClass = isLong ? 'question-text long-question' : 'question-text';
                
                return `
                    <div class="panel-card question-card-block" id="mock-q-block-${idx}" style="padding: 24px; margin-bottom: 12px; border: 2px solid var(--border-color); transition: border-color 0.2s;">
                        <div class="question-block-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; border-bottom: 1px solid var(--border-color); padding-bottom: 12px;">
                            <span class="mock-question-idx" style="font-size: 16px; font-weight: 700; color: var(--primary);">Câu hỏi ${idx + 1}</span>
                            ${isMultiSelect ? `<span class="multi-select-badge" style="font-size: 12px; font-weight: 600; padding: 4px 10px; background: rgba(59, 130, 246, 0.1); color: var(--primary); border-radius: 12px;">[Chọn nhiều]</span>` : ''}
                        </div>
                        <div class="${qTextClass}" style="font-size: 20px; font-weight: 500; line-height: 1.8; margin-bottom: 20px; white-space: normal; word-break: normal; overflow-wrap: break-word;">
                            ${formatMarkdown(q.question)}
                        </div>
                        <div class="options-container" style="display: flex; flex-direction: column; gap: 12px;">
                            ${q.options.map((opt, optIdx) => {
                                const letter = optionBadges[optIdx];
                                let isSelected = false;
                                if (isMultiSelect && Array.isArray(savedAnswer)) {
                                    isSelected = savedAnswer.includes(letter);
                                } else {
                                    isSelected = savedAnswer === letter;
                                }
                                
                                const checkIcon = isMultiSelect 
                                    ? `<span class="material-icons-round multi-check-icon" style="font-size:18px;margin-right:4px;">${isSelected ? 'check_box' : 'check_box_outline_blank'}</span>`
                                    : '';
                                
                                return `
                                    <div class="option-card ${isSelected ? 'selected' : ''}" 
                                         onclick="selectMockOptionScroll(${idx}, '${letter}', this)" 
                                         style="display: flex; align-items: center; gap: 16px; padding: 16px 20px; border-radius: var(--radius-md); border: 2px solid ${isSelected ? 'var(--primary)' : 'var(--border-color)'}; background: ${isSelected ? 'var(--bg-card-selected)' : 'var(--bg-card)'}; cursor: pointer; font-size: 16px; transition: all 0.15s; word-break: normal; overflow-wrap: break-word; white-space: normal; margin-bottom: 8px;">
                                        ${checkIcon}<div class="option-badge" style="width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px; background: ${isSelected ? 'var(--primary)' : 'var(--border-color)'}; color: ${isSelected ? 'white' : 'var(--text-main)'}; flex-shrink: 0;">${letter}</div>
                                        <div class="option-text" style="line-height: 1.6;">${opt}</div>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>
                `;
            }).join('')}
        </div>
    `;
}

function selectMockOptionScroll(qIdx, letter, optionEl) {
    const q = state.mock.questions[qIdx];
    const isMultiSelect = q.multiSelect === true;
    
    if (isMultiSelect) {
        let current = state.mock.userAnswers[qIdx];
        if (!Array.isArray(current)) current = [];
        
        const idx = current.indexOf(letter);
        if (idx > -1) {
            current.splice(idx, 1);
        } else {
            current.push(letter);
            current.sort();
        }
        state.mock.userAnswers[qIdx] = current.length > 0 ? current : undefined;
        if (current.length === 0) delete state.mock.userAnswers[qIdx];
    } else {
        state.mock.userAnswers[qIdx] = letter;
    }
    
    const block = document.getElementById(`mock-q-block-${qIdx}`);
    if (block) {
        const optionCards = block.querySelectorAll('.option-card');
        const savedAnswer = state.mock.userAnswers[qIdx];
        
        optionCards.forEach(card => {
            const badge = card.querySelector('.option-badge');
            if (!badge) return;
            const cardLetter = badge.textContent.trim();
            let isSelected = false;
            if (isMultiSelect && Array.isArray(savedAnswer)) {
                isSelected = savedAnswer.includes(cardLetter);
            } else {
                isSelected = savedAnswer === cardLetter;
            }
            
            if (isSelected) {
                card.classList.add('selected');
                card.style.borderColor = 'var(--primary)';
                card.style.background = 'var(--bg-card-selected)';
                if (isMultiSelect) {
                    const icon = card.querySelector('.multi-check-icon');
                    if (icon) icon.textContent = 'check_box';
                }
            } else {
                card.classList.remove('selected');
                card.style.borderColor = 'var(--border-color)';
                card.style.background = 'var(--bg-card)';
                if (isMultiSelect) {
                    const icon = card.querySelector('.multi-check-icon');
                    if (icon) icon.textContent = 'check_box_outline_blank';
                }
            }
            
            badge.style.background = isSelected ? 'var(--primary)' : 'var(--border-color)';
            badge.style.color = isSelected ? 'white' : 'var(--text-main)';
        });
    }
    
    updateMockQuestionMapStatus();
}

window.selectMockOptionScroll = selectMockOptionScroll;
window.renderMockQuestionsList = renderMockQuestionsList;

function renderMockQuestion() {
    renderMockQuestionsList();
}

function selectMockOption(letter) {
    // Legacy support
}

function navigateMockQuestion(direction) {
    // No-op in scrollable view
}

function jumpToMockQuestion(idx) {
    if (idx >= 0 && idx < state.mock.questions.length) {
        state.mock.currentIndex = idx;
        const el = document.getElementById(`mock-q-block-${idx}`);
        if (el) {
            el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            
            // Highlight temporarily
            el.style.borderColor = 'var(--primary)';
            setTimeout(() => {
                const isSelected = state.mock.userAnswers[idx] !== undefined;
                el.style.borderColor = isSelected ? 'var(--primary)' : 'var(--border-color)';
            }, 1000);
        }
        updateMockQuestionMapStatus();
    }
}

function submitMockExam(force = false) {
    if (!force) {
        const totalAnswered = Object.keys(state.mock.userAnswers).length;
        const totalQuestions = state.mock.questions.length;
        const confirmMsg = totalAnswered < totalQuestions 
            ? `Bạn mới trả lời ${totalAnswered}/${totalQuestions} câu. Bạn có chắc chắn muốn nộp bài thi không?` 
            : 'Bạn có chắc chắn muốn nộp bài thi thử này không?';
            
        if (!confirm(confirmMsg)) return;
    }
    
    clearMockTimer();
    state.mock.active = false;
    
    // Compute scores
    let correctCount = 0;
    const finalAnswersArray = []; // Map to 1-to-1 array for results panel
    
    state.mock.questions.forEach((q, idx) => {
        const userAns = state.mock.userAnswers[idx];
        const isMultiSelect = q.multiSelect === true;
        
        if (isMultiSelect) {
            // Multi-select: compare sorted arrays
            const userArr = Array.isArray(userAns) ? [...userAns].sort() : [];
            const correctArr = Array.isArray(q.correctAnswer) ? [...q.correctAnswer].sort() : [q.correctAnswer];
            finalAnswersArray.push(userArr.length > 0 ? userArr : '');
            
            const isCorrect = userArr.length === correctArr.length && userArr.every((v, i) => v === correctArr[i]);
            if (isCorrect) correctCount++;
            
            if (userArr.length > 0) {
                updateAnswerStatistics(q.topicId, isCorrect);
            }
        } else {
            // Single-select (original behavior)
            const ans = userAns || '';
            finalAnswersArray.push(ans);
            
            const isCorrect = ans === q.correctAnswer;
            if (isCorrect) correctCount++;
            
            if (ans) {
                updateAnswerStatistics(q.topicId, isCorrect);
            }
        }
    });
    
    const accuracy = Math.round((correctCount / state.mock.questions.length) * 100);
    
    // Save Mock Exam Stats
    const stats = storage.loadStats(state.currentSubjectId);
    stats.mockTaken++;
    stats.mockScores.push(accuracy);
    storage.saveStats(state.currentSubjectId, stats);
    
    // Calculate elapsed time
    const endTime = new Date();
    const elapsedSeconds = Math.round((endTime - state.mock.startTime) / 1000);
    const timeFormatted = `${Math.floor(elapsedSeconds / 60).toString().padStart(2, '0')}:${(elapsedSeconds % 60).toString().padStart(2, '0')}`;
    
    // Hide workspace, trigger results panel view
    document.getElementById('mock-exam-workspace-container').classList.add('hidden');
    document.getElementById('mock-setup-card').classList.remove('hidden');
    
    renderResultsPanel(correctCount, state.mock.questions.length, accuracy, timeFormatted, state.mock.questions, finalAnswersArray);
}

// ==========================================================================
// 5. RESULTS PANEL RENDER
// ==========================================================================
function renderResultsPanel(correct, total, accuracy, timeTaken, questions, userAnswers) {
    // Switch to results hash route directly without re-triggering prompt
    window.location.hash = '#results';
    
    // Render text metrics
    document.getElementById('result-correct-count').textContent = `${correct}/${total}`;
    document.getElementById('result-accuracy-percent').textContent = `${accuracy}%`;
    document.getElementById('result-time-taken').textContent = timeTaken ? timeTaken : '--:--';
    
    // Icon customization based on score
    const statusIcon = document.getElementById('result-status-icon');
    const mainTitle = document.getElementById('result-title-text');
    
    statusIcon.className = 'material-icons-round result-status-icon';
    
    if (accuracy >= 80) {
        statusIcon.classList.add('success');
        statusIcon.textContent = 'emoji_events';
        mainTitle.textContent = 'Xuất sắc!';
    } else if (accuracy >= 50) {
        statusIcon.classList.add('average');
        statusIcon.textContent = 'stars';
        mainTitle.textContent = 'Đạt yêu cầu!';
    } else {
        statusIcon.classList.add('failure');
        statusIcon.textContent = 'error_outline';
        mainTitle.textContent = 'Cần cố gắng thêm!';
    }
    
    // Suggestions analysis by topicId
    const incorrectTopics = {};
    
    // Render review items (Only show wrong or unchecked questions)
    const wrongSection = document.getElementById('wrong-questions-section');
    const wrongListContainer = document.getElementById('wrong-questions-list-container');
    
    wrongListContainer.innerHTML = '';
    
    questions.forEach((q, idx) => {
        const userAns = userAnswers[idx];
        const correctAns = q.correctAnswer;
        const isMultiSelect = q.multiSelect === true;
        
        let isCorrect;
        let userAnsDisplay;
        let correctAnsDisplay;
        
        const getOptDisplay = (l) => {
            if (!l || typeof l !== 'string' || l.length !== 1) return l || 'Chưa trả lời';
            const code = l.charCodeAt(0);
            const oIdx = (code >= 65 && code <= 90) ? code - 65 : -1;
            return (oIdx >= 0 && q.options && q.options[oIdx]) ? `${l} - ${q.options[oIdx]}` : l;
        };
        
        if (isMultiSelect) {
            const userArr = Array.isArray(userAns) ? [...userAns].sort() : [];
            const correctArr = Array.isArray(correctAns) ? [...correctAns].sort() : [correctAns];
            isCorrect = userArr.length === correctArr.length && userArr.every((v, i) => v === correctArr[i]);
            
            userAnsDisplay = userArr.length > 0 
                ? userArr.map(getOptDisplay).join(' | ')
                : 'Chưa trả lời';
            correctAnsDisplay = correctArr.map(getOptDisplay).join(' | ');
        } else {
            const ans = userAns || 'Chưa trả lời';
            isCorrect = ans === correctAns;
            userAnsDisplay = getOptDisplay(ans);
            correctAnsDisplay = getOptDisplay(correctAns);
        }
        
        // Track weak topics
        if (!isCorrect) {
            const tId = q.topicId || 'general';
            incorrectTopics[tId] = (incorrectTopics[tId] || 0) + 1;
        }
        
        const item = document.createElement('div');
        item.className = `review-item ${isCorrect ? 'correct' : 'incorrect'}`;
        
        const multiTag = isMultiSelect ? ' <span class="multi-select-tag">[Chọn nhiều]</span>' : '';
        
        if (isCorrect) {
            item.innerHTML = `
                <div class="review-q-text">Câu ${idx + 1}${multiTag}: ${formatMarkdown(q.question)}</div>
                <div class="review-answers">
                    <div class="review-user-ans correct" style="color: var(--success); display: flex; align-items: center; gap: 6px;">
                        <span class="material-icons-round" style="font-size:16px">check_circle</span>
                        Đáp án của bạn: ${userAnsDisplay} (Chính xác)
                    </div>
                </div>
                ${q.explanation ? `<div class="review-exp" style="border-left-color: var(--success);"><strong>Giải thích:</strong> ${formatMarkdown(q.explanation)}</div>` : ''}
            `;
        } else {
            item.innerHTML = `
                <div class="review-q-text">Câu ${idx + 1}${multiTag}: ${formatMarkdown(q.question)}</div>
                <div class="review-answers">
                    <div class="review-user-ans incorrect" style="color: var(--danger); display: flex; align-items: center; gap: 6px;">
                        <span class="material-icons-round" style="font-size:16px">cancel</span>
                        Đáp án của bạn: ${userAnsDisplay} (Không chính xác)
                    </div>
                    <div class="review-correct-ans" style="color: var(--success); display: flex; align-items: center; gap: 6px;">
                        <span class="material-icons-round" style="font-size:16px">check_circle</span>
                        Đáp án đúng: ${correctAnsDisplay}
                    </div>
                </div>
                ${q.explanation ? `<div class="review-exp"><strong>Giải thích:</strong> ${formatMarkdown(q.explanation)}</div>` : ''}
            `;
        }
        
        wrongListContainer.appendChild(item);
    });
    
    // Display suggestions
    const suggestionsContainer = document.getElementById('result-suggestions-container');
    const suggestionsList = document.getElementById('result-suggestions-list');
    
    if (suggestionsContainer && suggestionsList) {
        suggestionsList.innerHTML = '';
        const weakTopicIds = Object.keys(incorrectTopics).filter(tId => tId !== 'general' && tId !== 'undefined' && tId !== 'null');
        
        if (weakTopicIds.length > 0) {
            suggestionsContainer.classList.remove('hidden');
            
            weakTopicIds.forEach(topicId => {
                const topic = state.knowledgeData.find(t => t.topicId === topicId);
                const topicTitle = topic ? topic.title : 'Chủ đề ôn tập';
                const count = incorrectTopics[topicId];
                
                const item = document.createElement('div');
                item.className = 'suggestion-item';
                item.style.display = 'flex';
                item.style.alignItems = 'center';
                item.style.justifyContent = 'space-between';
                item.style.padding = '12px 16px';
                item.style.borderRadius = 'var(--radius-md)';
                item.style.background = 'var(--bg-card)';
                item.style.border = '1px solid var(--border-color)';
                item.style.marginBottom = '8px';
                
                item.innerHTML = `
                    <div style="display: flex; flex-direction: column; gap: 4px; text-align: left;">
                        <span style="font-weight: 700; font-size: 14.5px; color: var(--text-main);">${topicTitle}</span>
                        <span style="font-size: 12.5px; color: var(--danger); font-weight: 600;">Bạn làm sai ${count} câu ở phần này</span>
                    </div>
                    <button class="btn btn-primary btn-sm btn-icon" onclick="startPracticeForTopic('${topicId}')" style="font-size: 13px; padding: 8px 12px; height: auto;">
                        <span class="material-icons-round" style="font-size: 16px;">psychology</span> Ôn tập ngay
                    </button>
                `;
                suggestionsList.appendChild(item);
            });
        } else {
            suggestionsContainer.classList.add('hidden');
        }
    }
    
    wrongSection.classList.remove('hidden');
}

// ==========================================================================
// 6. ANALYTICS PANEL & SVG CHARTING
// ==========================================================================
function renderAnalyticsScreen() {
    if (!state.currentSubjectId) return;
    
    const stats = storage.loadStats(state.currentSubjectId);
    const readList = storage.loadReadTopics(state.currentSubjectId);
    
    // Top summary counters
    const topicsRead = readList.filter(id => state.knowledgeData.some(t => t.topicId === id)).length;
    document.getElementById('analytics-topics-read').textContent = `${topicsRead}/${state.knowledgeData.length}`;
    document.getElementById('analytics-quizzes-taken').textContent = stats.quizzesTaken || 0;
    document.getElementById('analytics-mock-taken').textContent = stats.mockTaken || 0;
    
    // Calculate average mock scores
    let avg = 0;
    if (stats.mockScores && stats.mockScores.length > 0) {
        const sum = stats.mockScores.reduce((a, b) => a + b, 0);
        avg = Math.round(sum / stats.mockScores.length);
    }
    document.getElementById('analytics-avg-score').textContent = `${avg}%`;
    
    // Generate Strengths & Weaknesses Columns
    const strengthsList = document.getElementById('analytics-strengths-list');
    const weaknessesList = document.getElementById('analytics-weaknesses-list');
    
    strengthsList.innerHTML = '';
    weaknessesList.innerHTML = '';
    
    let strengthsCount = 0;
    let weaknessesCount = 0;
    
    state.knowledgeData.forEach(topic => {
        const tStats = stats.topicStats[topic.topicId];
        let pct = 0;
        let answered = false;
        
        if (tStats && tStats.total > 0) {
            pct = Math.round((tStats.correct / tStats.total) * 100);
            answered = true;
        }
        
        const card = document.createElement('div');
        card.className = 'perf-item';
        
        // Define if strength (>=70% accuracy) or weakness (<70% accuracy)
        const isStrength = answered && pct >= 70;
        
        card.innerHTML = `
            <div class="perf-title">${topic.title}</div>
            <div class="perf-progress-wrapper">
                <div class="perf-bar-bg">
                    <div class="perf-bar-fill ${isStrength ? 'success' : 'danger'}" style="width: ${answered ? pct : 0}%"></div>
                </div>
                <span class="perf-percent ${isStrength ? 'success' : 'danger'}">
                    ${answered ? `${pct}%` : 'Chưa ôn'}
                </span>
            </div>
        `;
        
        if (isStrength) {
            strengthsList.appendChild(card);
            strengthsCount++;
        } else {
            weaknessesList.appendChild(card);
            weaknessesCount++;
        }
    });
    
    if (strengthsCount === 0) {
        strengthsList.innerHTML = '<div class="empty-list-info">Chưa có chủ đề nào đạt yêu cầu (≥ 70%). Hãy ôn tập thêm!</div>';
    }
    
    if (weaknessesCount === 0) {
        weaknessesList.innerHTML = '<div class="empty-list-info">Tuyệt vời! Không có chủ đề nào dưới mức yêu cầu.</div>';
    }
    
    // Render custom programmatical SVG Chart of topic accuracies
    renderAnalyticsSVGChart(stats);
}

function renderAnalyticsSVGChart(stats) {
    const svg = document.getElementById('analytics-chart-svg');
    const emptyMsg = document.getElementById('chart-empty-message');
    if (!svg) return;
    
    // Clear old elements
    svg.innerHTML = '';
    
    // Filter out topics with data
    const activeTopics = state.knowledgeData.map(topic => {
        const tStats = stats.topicStats[topic.topicId];
        return {
            title: topic.title,
            accuracy: tStats && tStats.total > 0 ? Math.round((tStats.correct / tStats.total) * 100) : 0,
            hasData: tStats && tStats.total > 0
        };
    }).filter(t => t.hasData);
    
    if (activeTopics.length === 0) {
        emptyMsg.classList.remove('hidden');
        svg.style.display = 'none';
        return;
    }
    
    emptyMsg.classList.add('hidden');
    svg.style.display = 'block';
    
    // Constants for charting sizes
    const paddingLeft = 140;
    const paddingRight = 40;
    const paddingTop = 20;
    const paddingBottom = 20;
    const rowHeight = 35;
    
    const chartWidth = 400;
    const chartHeight = activeTopics.length * rowHeight + paddingTop + paddingBottom;
    
    svg.setAttribute('viewBox', `0 0 ${chartWidth} ${chartHeight}`);
    svg.style.height = `${chartHeight}px`;
    
    // Injected Definitions (Gradients)
    svg.innerHTML = `
        <defs>
            <linearGradient id="chart-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="var(--primary)" />
                <stop offset="100%" stop-color="var(--secondary)" />
            </linearGradient>
        </defs>
    `;
    
    // Draw gridlines
    const gridPoints = [0, 25, 50, 75, 100];
    const availableWidth = chartWidth - paddingLeft - paddingRight;
    
    gridPoints.forEach(val => {
        const x = paddingLeft + (val / 100) * availableWidth;
        
        // Line
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', x);
        line.setAttribute('y1', paddingTop);
        line.setAttribute('x2', x);
        line.setAttribute('y2', chartHeight - paddingBottom);
        line.className.baseVal = 'chart-grid-line';
        svg.appendChild(line);
        
        // Label text at bottom
        const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        txt.setAttribute('x', x);
        txt.setAttribute('y', chartHeight - paddingBottom + 14);
        txt.setAttribute('text-anchor', 'middle');
        txt.className.baseVal = 'chart-text';
        txt.textContent = `${val}%`;
        svg.appendChild(txt);
    });
    
    // Draw bars
    activeTopics.forEach((topic, idx) => {
        const y = paddingTop + idx * rowHeight + 10;
        
        // Text label
        const txtLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        txtLabel.setAttribute('x', paddingLeft - 10);
        txtLabel.setAttribute('y', y + 10);
        txtLabel.setAttribute('text-anchor', 'end');
        txtLabel.className.baseVal = 'chart-text';
        // Truncate text if too long
        let shortTitle = topic.title;
        if (shortTitle.length > 18) shortTitle = shortTitle.slice(0, 16) + '...';
        txtLabel.textContent = shortTitle;
        svg.appendChild(txtLabel);
        
        // Bar background
        const barBg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        barBg.setAttribute('x', paddingLeft);
        barBg.setAttribute('y', y);
        barBg.setAttribute('width', availableWidth);
        barBg.setAttribute('height', 14);
        barBg.className.baseVal = 'chart-bar-bg';
        svg.appendChild(barBg);
        
        // Bar fill
        const barFill = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        barFill.setAttribute('x', paddingLeft);
        barFill.setAttribute('y', y);
        barFill.setAttribute('width', (topic.accuracy / 100) * availableWidth);
        barFill.setAttribute('height', 14);
        barFill.className.baseVal = 'chart-bar-fill';
        svg.appendChild(barFill);
        
        // Accuracy label inside / beside bar
        const valLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        valLabel.setAttribute('x', paddingLeft + (topic.accuracy / 100) * availableWidth + 8);
        valLabel.setAttribute('y', y + 11);
        valLabel.className.baseVal = 'chart-text';
        valLabel.style.fontWeight = 'bold';
        valLabel.style.fill = 'var(--text-main)';
        valLabel.textContent = `${topic.accuracy}%`;
        svg.appendChild(valLabel);
    });
}

// ==========================================================================
// TOAST NOTIFICATIONS & UTILS
// ==========================================================================
function showToast(message, type = 'info') {
    const container = document.getElementById('toast-notifications');
    if (!container) return;
    
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    // Choose icons based on type
    const icons = {
        'success': 'check_circle',
        'warning': 'warning',
        'danger': 'error',
        'info': 'info'
    };
    
    toast.innerHTML = `
        <span class="material-icons-round">${icons[type] || 'info'}</span>
        <span>${message}</span>
    `;
    
    container.appendChild(toast);
    
    // Trigger fadeout after 2.7s
    setTimeout(() => {
        toast.classList.add('fade-out');
        // Delete from DOM after transition finishes
        toast.addEventListener('animationend', () => {
            toast.remove();
        });
    }, 2700);
}

// Array shuffling utility (Fisher-Yates Algorithm)
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// ==========================================================================
// CUSTOM PREMIUM SELECT DROPDOWNS
// ==========================================================================
function initCustomSelects() {
    // Add global click listener to close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        const activeTriggers = document.querySelectorAll('.custom-select-trigger.open');
        activeTriggers.forEach(trigger => {
            const selectId = trigger.dataset.selectId;
            const customSelect = trigger.closest('.custom-select');
            if (customSelect && !customSelect.contains(e.target)) {
                trigger.classList.remove('open');
                const optionsPanel = customSelect.querySelector('.custom-select-options');
                if (optionsPanel) optionsPanel.classList.remove('show');
            }
        });
    });
}

function syncCustomSelect(selectId) {
    const nativeSelect = document.getElementById(selectId);
    if (!nativeSelect) return;

    const container = nativeSelect.closest('.custom-select');
    if (!container) return;

    // Remove old arrow if present
    const nativeArrow = container.querySelector('.select-arrow');
    if (nativeArrow) nativeArrow.style.display = 'none';

    // Get or create trigger
    let trigger = container.querySelector('.custom-select-trigger');
    if (!trigger) {
        trigger = document.createElement('div');
        trigger.className = 'custom-select-trigger';
        trigger.dataset.selectId = selectId;
        
        const valueSpan = document.createElement('span');
        valueSpan.className = 'custom-select-value';
        
        const arrowSpan = document.createElement('span');
        arrowSpan.className = 'material-icons-round custom-select-arrow';
        arrowSpan.textContent = 'expand_more';
        
        trigger.appendChild(valueSpan);
        trigger.appendChild(arrowSpan);
        container.appendChild(trigger);

        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            // Close other open custom selects
            document.querySelectorAll('.custom-select-trigger').forEach(otherTrigger => {
                if (otherTrigger !== trigger && otherTrigger.classList.contains('open')) {
                    otherTrigger.classList.remove('open');
                    const otherOptions = otherTrigger.closest('.custom-select').querySelector('.custom-select-options');
                    if (otherOptions) otherOptions.classList.remove('show');
                }
            });
            
            trigger.classList.toggle('open');
            const optionsPanel = container.querySelector('.custom-select-options');
            if (optionsPanel) optionsPanel.classList.toggle('show');
        });
    }

    // Get or create options panel
    let optionsPanel = container.querySelector('.custom-select-options');
    if (!optionsPanel) {
        optionsPanel = document.createElement('div');
        optionsPanel.className = 'custom-select-options';
        optionsPanel.dataset.selectId = selectId;
        container.appendChild(optionsPanel);
    }

    // Update selection value display
    const selectedOption = nativeSelect.options[nativeSelect.selectedIndex];
    const valueSpan = trigger.querySelector('.custom-select-value');
    if (valueSpan) {
        valueSpan.textContent = selectedOption ? selectedOption.textContent : 'Chọn...';
    }

    // Rebuild options
    optionsPanel.innerHTML = '';
    Array.from(nativeSelect.options).forEach(option => {
        const optDiv = document.createElement('div');
        optDiv.className = 'custom-select-option';
        if (option.value === nativeSelect.value) {
            optDiv.classList.add('active');
        }
        optDiv.textContent = option.textContent;
        optDiv.dataset.value = option.value;

        optDiv.addEventListener('click', (e) => {
            e.stopPropagation();
            nativeSelect.value = option.value;
            // Dispatch change event to trigger native event handlers
            nativeSelect.dispatchEvent(new Event('change'));
            
            // Sync selection visual
            valueSpan.textContent = option.textContent;
            optionsPanel.querySelectorAll('.custom-select-option').forEach(o => o.classList.remove('active'));
            optDiv.classList.add('active');
            
            // Close dropdown
            trigger.classList.remove('open');
            optionsPanel.classList.remove('show');
        });

        optionsPanel.appendChild(optDiv);
    });
}

// ==========================================================================
// INTERACTIVE AND-OR TREE PRACTICE GAME
// ==========================================================================
const interactiveExercises = {
    ex1: {
        title: "Bài 1: AND-OR Graph (Slide Ch. 7, p. 9)",
        initialState: "S",
        goal: ["B", "D", "E", "G"],
        rules: [
            { id: "R1", source: "S", targets: ["A", "B"], type: "AND" },
            { id: "R2", source: "S", targets: ["C"], type: "OR" },
            { id: "R3", source: "A", targets: ["D", "E"], type: "AND" },
            { id: "R4", source: "F", targets: ["G", "E"], type: "AND" },
            { id: "R5", source: "F", targets: ["H"], type: "OR" },
            { id: "R6", source: "C", targets: ["F"], type: "OR" }
        ],
        correctLinks: {
            "S": ["A", "B"],
            "A": ["D", "E"],
            "F": ["G", "E"]
        },
        correctRelations: {
            "S": "AND",
            "A": "AND",
            "F": "AND"
        },
        nodes: [
            { id: "S", x: 60, y: 220 },
            { id: "A", x: 200, y: 100 },
            { id: "B", x: 200, y: 220 },
            { id: "C", x: 200, y: 340 },
            { id: "D", x: 340, y: 50 },
            { id: "E", x: 340, y: 150 },
            { id: "F", x: 340, y: 340 },
            { id: "G", x: 480, y: 260 },
            { id: "H", x: 480, y: 380 }
        ]
    },
    ex2: {
        title: "Bài 2: Non-deterministic Search (Slide Ch. 7, p. 31)",
        initialState: "S",
        goal: ["D", "G", "H"],
        rules: [
            { id: "R1", source: "S", targets: ["A", "B", "C"], type: "AND" },
            { id: "R2", source: "A", targets: ["D"], type: "OR" },
            { id: "R3", source: "B", targets: ["E", "F"], type: "AND" },
            { id: "R4", source: "C", targets: ["D", "G"], type: "AND" },
            { id: "R5", source: "F", targets: ["H"], type: "OR" }
        ],
        correctLinks: {
            "S": ["A", "B", "C"],
            "B": ["E", "F"],
            "C": ["D", "G"]
        },
        correctRelations: {
            "S": "AND",
            "B": "AND",
            "C": "AND"
        },
        nodes: [
            { id: "S", x: 60, y: 220 },
            { id: "A", x: 200, y: 100 },
            { id: "B", x: 200, y: 220 },
            { id: "C", x: 200, y: 340 },
            { id: "D", x: 340, y: 60 },
            { id: "E", x: 340, y: 170 },
            { id: "F", x: 340, y: 270 },
            { id: "G", x: 340, y: 380 },
            { id: "H", x: 480, y: 270 }
        ]
    },
    ex3: {
        title: "Bài 3: Conditional Plan Search (Slide Ch. 8, p. 2)",
        initialState: "S",
        goal: ["H", "F"],
        rules: [
            { id: "R1", source: "S", targets: ["A"], type: "OR" },
            { id: "R2", source: "S", targets: ["B"], type: "OR" },
            { id: "R3", source: "A", targets: ["C", "D"], type: "AND" },
            { id: "R4", source: "B", targets: ["D", "E", "F"], type: "AND" },
            { id: "R5", source: "C", targets: ["G"], type: "OR" },
            { id: "R6", source: "D", targets: ["H"], type: "OR" },
            { id: "R7", source: "E", targets: ["H"], type: "OR" },
            { id: "R8", source: "E", targets: ["K"], type: "OR" }
        ],
        correctLinks: {
            "S": ["A", "B"],
            "A": ["C", "D"],
            "B": ["D", "E", "F"]
        },
        correctRelations: {
            "S": "OR",
            "A": "AND",
            "B": "AND"
        },
        nodes: [
            { id: "S", x: 60, y: 220 },
            { id: "A", x: 190, y: 110 },
            { id: "B", x: 190, y: 330 },
            { id: "C", x: 320, y: 50 },
            { id: "D", x: 320, y: 220 },
            { id: "E", x: 320, y: 350 },
            { id: "F", x: 320, y: 450 },
            { id: "G", x: 460, y: 50 },
            { id: "H", x: 460, y: 250 },
            { id: "K", x: 460, y: 400 }
        ]
    },
    ex4: {
        title: "Bài 4: Simple AND-OR Graph (Slide Ch. 7, p. 11)",
        initialState: "a",
        goal: ["b", "c"],
        rules: [
            { id: "R1", source: "a", targets: ["b", "c"], type: "AND" },
            { id: "R2", source: "a", targets: ["d"], type: "OR" }
        ],
        correctLinks: {
            "a": ["b", "c", "d"]
        },
        correctRelations: {
            "a": "OR"
        },
        nodes: [
            { id: "a", x: 100, y: 220 },
            { id: "b", x: 260, y: 120 },
            { id: "d", x: 260, y: 220 },
            { id: "c", x: 260, y: 320 }
        ]
    },
    ex5: {
        title: "Bài 5: Multi-layer AND-OR Graph",
        initialState: "S",
        goal: ["G"],
        rules: [
            { id: "R1", source: "S", targets: ["A", "B"], type: "AND" },
            { id: "R2", source: "A", targets: ["C"], type: "OR" },
            { id: "R3", source: "B", targets: ["D"], type: "OR" },
            { id: "R4", source: "C", targets: ["G"], type: "OR" },
            { id: "R5", source: "D", targets: ["G"], type: "OR" }
        ],
        correctLinks: {
            "S": ["A", "B"],
            "A": ["C"],
            "B": ["D"],
            "C": ["G"],
            "D": ["G"]
        },
        correctRelations: {
            "S": "AND",
            "A": "OR",
            "B": "OR",
            "C": "OR",
            "D": "OR"
        },
        nodes: [
            { id: "S", x: 80, y: 220 },
            { id: "A", x: 200, y: 120 },
            { id: "B", x: 200, y: 320 },
            { id: "C", x: 320, y: 120 },
            { id: "D", x: 320, y: 320 },
            { id: "G", x: 460, y: 220 }
        ]
    }
};

const interactiveState = {
    currentExId: 'ex1',
    userConnections: {}, // parentNodeId -> array of childNodeIds
    userRelations: {}, // parentNodeId -> 'AND' or 'OR'
    selectedSourceNode: null,
    simulationActive: false,
    initialized: false
};

function renderInteractivePracticeScreen() {
    const nonAiAlert = document.getElementById('interactive-non-ai-alert');
    const aiWorkspace = document.getElementById('interactive-ai-workspace');
    
    if (!nonAiAlert || !aiWorkspace) return;
    
    if (state.currentSubjectId !== 'trituenhantao-ontap') {
        nonAiAlert.classList.remove('hidden');
        aiWorkspace.classList.add('hidden');
        
        const btnSwitch = document.getElementById('btn-switch-to-ai');
        if (btnSwitch) {
            btnSwitch.onclick = async () => {
                const aiSubject = state.subjects.find(s => s.id === 'trituenhantao-ontap');
                if (aiSubject) {
                    await selectSubject('trituenhantao-ontap');
                    renderInteractivePracticeScreen();
                } else {
                    showToast('Không tìm thấy dữ liệu môn Trí Tuệ Nhân Tạo.', 'danger');
                }
            };
        }
        return;
    }
    
    nonAiAlert.classList.add('hidden');
    aiWorkspace.classList.remove('hidden');
    
    if (!interactiveState.initialized) {
        setupInteractiveEventListeners();
        interactiveState.initialized = true;
    }
    
    initInteractiveExercise(interactiveState.currentExId);
}

function setupInteractiveEventListeners() {
    const exSelect = document.getElementById('interactive-ex-select');
    if (exSelect) {
        exSelect.addEventListener('change', (e) => {
            interactiveState.currentExId = e.target.value;
            initInteractiveExercise(interactiveState.currentExId);
        });
    }
    
    const btnReset = document.getElementById('btn-reset-graph');
    if (btnReset) {
        btnReset.addEventListener('click', () => {
            initInteractiveExercise(interactiveState.currentExId);
            showToast('Đã đặt lại đồ thị bài tập.', 'info');
        });
    }

    const btnConnect = document.getElementById('btn-connect-nodes');
    if (btnConnect) {
        btnConnect.addEventListener('click', () => {
            if (interactiveState.simulationActive) return;
            const parentVal = document.getElementById('parent-node-select').value;
            const childVal = document.getElementById('child-node-select').value;
            const groupVal = document.getElementById('rule-group-select').value || 'R1';
            
            if (!parentVal || !childVal) {
                showToast('Vui lòng chọn cả node cha và node con!', 'warning');
                return;
            }
            if (parentVal === childVal) {
                showToast('Không thể nối một nút với chính nó!', 'warning');
                return;
            }
            
            if (!interactiveState.userConnections[parentVal]) {
                interactiveState.userConnections[parentVal] = {};
            }
            if (!interactiveState.userConnections[parentVal][groupVal]) {
                interactiveState.userConnections[parentVal][groupVal] = [];
            }
            
            if (!interactiveState.userConnections[parentVal][groupVal].includes(childVal)) {
                interactiveState.userConnections[parentVal][groupVal].push(childVal);
                showToast(`Đã nối ${parentVal} ➔ ${childVal} (Luật ${groupVal})`, 'success');
            } else {
                showToast(`Liên kết ${parentVal} ➔ ${childVal} đã tồn tại trong nhóm này!`, 'warning');
            }
            drawInteractiveGraph();
            renderAndOrRadios();
        });
    }

    const btnDisconnect = document.getElementById('btn-disconnect-nodes');
    if (btnDisconnect) {
        btnDisconnect.addEventListener('click', () => {
            if (interactiveState.simulationActive) return;
            const parentVal = document.getElementById('parent-node-select').value;
            const childVal = document.getElementById('child-node-select').value;
            const groupVal = document.getElementById('rule-group-select').value || 'R1';
            
            if (!parentVal || !childVal) {
                showToast('Vui lòng chọn cả node cha và con để ngắt kết nối!', 'warning');
                return;
            }
            if (interactiveState.userConnections[parentVal] && interactiveState.userConnections[parentVal][groupVal]) {
                const initialLen = interactiveState.userConnections[parentVal][groupVal].length;
                interactiveState.userConnections[parentVal][groupVal] = interactiveState.userConnections[parentVal][groupVal].filter(c => c !== childVal);
                
                if (interactiveState.userConnections[parentVal][groupVal].length < initialLen) {
                    showToast(`Đã xóa liên kết ${parentVal} ➔ ${childVal} (Luật ${groupVal})`, 'info');
                }
                
                if (interactiveState.userConnections[parentVal][groupVal].length === 0) {
                    delete interactiveState.userConnections[parentVal][groupVal];
                    if (interactiveState.userRelations[parentVal]) {
                        delete interactiveState.userRelations[parentVal][groupVal];
                    }
                }
                if (Object.keys(interactiveState.userConnections[parentVal]).length === 0) {
                    delete interactiveState.userConnections[parentVal];
                    delete interactiveState.userRelations[parentVal];
                }
            }
            drawInteractiveGraph();
            renderAndOrRadios();
        });
    }

    const btnSubmit = document.getElementById('btn-submit-workspace-solve');
    if (btnSubmit) {
        btnSubmit.addEventListener('click', () => {
            submitWorkspaceSolve();
        });
    }

    // Mode toggles
    const modeRadios = document.querySelectorAll('input[name="workspace-mode"]');
    modeRadios.forEach(radio => {
        radio.addEventListener('change', () => {
            initInteractiveExercise(interactiveState.currentExId);
        });
    });
}

function initInteractiveExercise(exId) {
    const ex = interactiveExercises[exId];
    if (!ex) return;
    
    interactiveState.userConnections = {};
    interactiveState.userRelations = {};
    interactiveState.selectedSourceNode = null;
    interactiveState.simulationActive = false;
    
    // Hide simulation log section
    document.getElementById('simulation-validation-card').classList.add('hidden');
    document.getElementById('simulation-summary-box').classList.add('hidden');
    document.getElementById('simulation-log-list').innerHTML = '';
    
    // Clear prediction radio buttons
    const predictionRadios = document.querySelectorAll('input[name="solvability-prediction"]');
    predictionRadios.forEach(r => r.checked = false);
    
    // Hide split screen
    const correctCanvas = document.getElementById('correct-canvas-area');
    const userLabel = document.getElementById('user-canvas-label');
    if (correctCanvas) correctCanvas.classList.add('hidden');
    if (userLabel) userLabel.classList.add('hidden');

    // Get current mode
    const mode = document.querySelector('input[name="workspace-mode"]:checked')?.value || 'practice';

    // Populate dropdown options
    const parentSelect = document.getElementById('parent-node-select');
    const childSelect = document.getElementById('child-node-select');
    if (parentSelect && childSelect) {
        parentSelect.innerHTML = '';
        childSelect.innerHTML = '';
        ex.nodes.forEach(n => {
            const opt1 = document.createElement('option');
            opt1.value = n.id;
            opt1.textContent = n.id;
            parentSelect.appendChild(opt1);

            const opt2 = document.createElement('option');
            opt2.value = n.id;
            opt2.textContent = n.id;
            childSelect.appendChild(opt2);
        });
    }

    // Step 1: Render description outline
    const exDesc = document.getElementById('ex-description');
    if (exDesc) {
        if (mode === 'practice') {
            let rulesHtml = ex.rules.map(r => `<div><strong>${r.id}:</strong> ${r.source} &rarr; ${r.targets.join(', ')}</div>`).join('');
            exDesc.innerHTML = `
                <h4 style="margin-bottom: 8px; color: var(--primary);">${ex.title}</h4>
                <p style="font-size: 13.5px; color: var(--text-muted); margin-bottom: 10px;">Dưới đây là danh sách các luật chuyển trạng thái ban đầu (không hiển thị quan hệ AND/OR). Hãy xây dựng đồ thị lời giải bằng bảng điều khiển bên phải.</p>
                <div style="background: var(--bg-app); padding: 12px; border-radius: var(--radius-sm); font-family: monospace; font-size: 13px; line-height: 1.5; color: var(--text-main); border: 1.5px dashed var(--border-color); display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                    ${rulesHtml}
                </div>
            `;
        } else {
            exDesc.innerHTML = `
                <h4 style="margin-bottom: 8px; color: var(--primary);">${ex.title} (CHẾ ĐỘ KIỂM TRA)</h4>
                <p style="font-size: 13.5px; color: var(--text-muted);">Mọi gợi ý và lời giải mẫu bị ẩn. Hãy tự kết nối đồ thị, xác định quan hệ AND/OR, chọn tính khả thi và nộp bài để xem chấm.</p>
            `;
        }
    }

    // Step 4: Show Goal state info
    const goalDisplay = document.getElementById('goal-info-display');
    if (goalDisplay) {
        goalDisplay.textContent = `Goal = { ${ex.goal.join(', ')} }`;
    }

    renderCanvasNodes(ex.nodes);
    renderAndOrRadios();
    drawInteractiveGraph();
}

function renderCanvasNodes(nodes, containerId = 'interactive-nodes-container', isUserGraph = true) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = '';
    
    nodes.forEach(node => {
        const div = document.createElement('div');
        div.className = 'interactive-node';
        div.id = isUserGraph ? `node-${node.id}` : `correct-node-${node.id}`;
        div.textContent = node.id;
        div.style.left = `${node.x}px`;
        div.style.top = `${node.y}px`;
        div.style.position = 'absolute';
        div.style.width = '55px';
        div.style.height = '55px';
        div.style.borderRadius = '50%';
        div.style.background = 'var(--bg-card)';
        div.style.border = '2.5px solid var(--border-color)';
        div.style.color = 'var(--text-main)';
        div.style.display = 'flex';
        div.style.justifyContent = 'center';
        div.style.alignItems = 'center';
        div.style.fontWeight = '700';
        div.style.cursor = isUserGraph ? 'pointer' : 'default';
        div.style.boxShadow = 'var(--shadow-sm)';
        div.style.transition = 'all 0.2s ease';
        div.style.zIndex = '5';
        
        if (isUserGraph) {
            div.addEventListener('click', () => {
                if (interactiveState.simulationActive) return;
                // Set as parent in dropdown when clicked
                const parentSelect = document.getElementById('parent-node-select');
                if (parentSelect) {
                    parentSelect.value = node.id;
                }
            });
        }
        
        container.appendChild(div);
    });
}

function renderAndOrRadios() {
    const container = document.getElementById('and-or-radio-container');
    if (!container) return;
    container.innerHTML = '';

    const parentNodes = Object.keys(interactiveState.userConnections);
    if (parentNodes.length === 0) {
        container.innerHTML = `<p style="font-size: 12px; color: var(--text-muted); font-style: italic;">Chưa có nút cha nào có liên kết.</p>`;
        return;
    }

    parentNodes.sort().forEach(p => {
        const groups = interactiveState.userConnections[p];
        Object.keys(groups).sort().forEach(g => {
            const children = groups[g];
            if (!children || children.length === 0) return;
            
            if (!interactiveState.userRelations[p]) interactiveState.userRelations[p] = {};
            const currentRel = interactiveState.userRelations[p][g] || 'OR';
            
            const row = document.createElement('div');
            row.style.display = 'flex';
            row.style.alignItems = 'center';
            row.style.justifyContent = 'space-between';
            row.style.background = 'var(--bg-app)';
            row.style.padding = '6px 12px';
            row.style.borderRadius = 'var(--radius-sm)';
            row.style.fontSize = '13px';
            row.style.border = '1px solid var(--border-color)';
            row.style.marginBottom = '6px';
            
            row.innerHTML = `
                <span style="font-weight: 600;">Node ${p} (${g}) &rarr; (${children.join(', ')})</span>
                <div style="display: flex; gap: 10px;">
                    <label style="cursor: pointer; display: flex; align-items: center; gap: 3px;">
                        <input type="radio" name="rel-${p}-${g}" value="OR" ${currentRel === 'OR' ? 'checked' : ''}> OR
                    </label>
                    <label style="cursor: pointer; display: flex; align-items: center; gap: 3px;">
                        <input type="radio" name="rel-${p}-${g}" value="AND" ${currentRel === 'AND' ? 'checked' : ''}> AND
                    </label>
                </div>
            `;
            
            row.querySelectorAll(`input[name="rel-${p}-${g}"]`).forEach(radio => {
                radio.addEventListener('change', (e) => {
                    interactiveState.userRelations[p][g] = e.target.value;
                    drawInteractiveGraph();
                });
            });
            
            if (!interactiveState.userRelations[p][g]) {
                interactiveState.userRelations[p][g] = 'OR';
            }
            
            container.appendChild(row);
        });
    });
}

function drawInteractiveGraph() {
    const ex = interactiveExercises[interactiveState.currentExId];
    if (!ex) return;
    drawGraphOnSvg('interactive-svg-overlay', interactiveState.userConnections, interactiveState.userRelations, ex);
}

function drawCorrectGraph() {
    const ex = interactiveExercises[interactiveState.currentExId];
    if (!ex) return;
    
    // Build correct grouped connections from rules
    const correctConn = {};
    const correctRel = {};
    
    ex.rules.forEach(r => {
        const p = r.source;
        const g = r.id; // rule ID as group
        if (!correctConn[p]) correctConn[p] = {};
        if (!correctRel[p]) correctRel[p] = {};
        
        correctConn[p][g] = [...r.targets];
        // If targets > 1, it's AND, else OR
        correctRel[p][g] = r.targets.length > 1 ? 'AND' : 'OR';
    });
    
    renderCanvasNodes(ex.nodes, 'correct-nodes-container', false);
    drawGraphOnSvg('correct-svg-overlay', correctConn, correctRel, ex);
}

function drawGraphOnSvg(svgId, connections, relations, ex) {
    const svg = document.getElementById(svgId);
    if (!svg) return;
    svg.innerHTML = '';
    
    const nodeCoords = {};
    ex.nodes.forEach(n => {
        nodeCoords[n.id] = { x: n.x + 27.5, y: n.y + 27.5 };
    });
    
    // Draw connections
    Object.keys(connections).forEach(p => {
        const groups = connections[p];
        Object.keys(groups).forEach(g => {
            const children = groups[g];
            if (children.length === 0) return;
            
            const isAnd = relations[p] && relations[p][g] === 'AND';
            const ruleLabel = g;
            
            if (isAnd) {
                const start = nodeCoords[p];
                // Calculate intermediate point
                let avgX = 0, avgY = 0;
                children.forEach(c => {
                    avgX += nodeCoords[c].x;
                    avgY += nodeCoords[c].y;
                });
                avgX /= children.length;
                avgY /= children.length;
                
                const angle = Math.atan2(avgY - start.y, avgX - start.x);
                const dist = 50; // Distance to intermediate node
                const midX = start.x + Math.cos(angle) * dist;
                const midY = start.y + Math.sin(angle) * dist;
                
                // Draw arrow from parent to mid
                const startEdgeX = start.x + Math.cos(angle) * 27.5;
                const startEdgeY = start.y + Math.sin(angle) * 27.5;
                const midEdgeX = midX - Math.cos(angle) * 10; // leave space for dot
                const midEdgeY = midY - Math.sin(angle) * 10;
                
                const lineToMid = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                lineToMid.setAttribute('x1', startEdgeX);
                lineToMid.setAttribute('y1', startEdgeY);
                lineToMid.setAttribute('x2', midEdgeX);
                lineToMid.setAttribute('y2', midEdgeY);
                lineToMid.setAttribute('stroke', 'var(--primary)');
                lineToMid.setAttribute('stroke-width', '2.5');
                lineToMid.setAttribute('marker-end', 'url(#arrow)');
                svg.appendChild(lineToMid);
                
                // Note: Removed the text label on the line to avoid overlap. We only show it on the dot.
                
                // Draw intermediate dot
                const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                dot.setAttribute('cx', midX);
                dot.setAttribute('cy', midY);
                dot.setAttribute('r', '6'); // make dot a bit larger
                dot.setAttribute('fill', 'var(--bg-card)');
                dot.setAttribute('stroke', 'var(--primary)');
                dot.setAttribute('stroke-width', '2.5');
                svg.appendChild(dot);
                
                // Draw intermediate node name (e.g. R1')
                const dotText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                dotText.setAttribute('x', midX + 12);
                dotText.setAttribute('y', midY + 6);
                dotText.setAttribute('fill', 'var(--text-main)');
                dotText.setAttribute('font-size', '14px'); // larger font
                dotText.setAttribute('font-weight', 'bold');
                dotText.textContent = ruleLabel + '\'';
                svg.appendChild(dotText);
                
                // Draw lines from mid to children
                children.forEach(c => {
                    const end = nodeCoords[c];
                    const childAngle = Math.atan2(end.y - midY, end.x - midX);
                    const endEdgeX = end.x - Math.cos(childAngle) * 31.5;
                    const endEdgeY = end.y - Math.sin(childAngle) * 31.5;
                    
                    const lineFromMid = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                    lineFromMid.setAttribute('x1', midX + Math.cos(childAngle) * 8);
                    lineFromMid.setAttribute('y1', midY + Math.sin(childAngle) * 8);
                    lineFromMid.setAttribute('x2', endEdgeX);
                    lineFromMid.setAttribute('y2', endEdgeY);
                    lineFromMid.setAttribute('stroke', 'var(--primary)');
                    lineFromMid.setAttribute('stroke-width', '2.5');
                    lineFromMid.setAttribute('marker-end', 'url(#arrow)');
                    svg.appendChild(lineFromMid);
                });
                
                // Draw AND arc around mid node
                if (children.length >= 2) {
                    const targets = children.map(c => nodeCoords[c]).filter(t => !!t);
                    const angles = targets.map(t => Math.atan2(t.y - midY, t.x - midX));
                    angles.sort((a, b) => a - b);
                    
                    const arcDist = 30;
                    const arcPoints = angles.map(a => ({
                        x: midX + Math.cos(a) * arcDist,
                        y: midY + Math.sin(a) * arcDist
                    }));
                    
                    let pathD = `M ${arcPoints[0].x} ${arcPoints[0].y}`;
                    for (let i = 1; i < arcPoints.length; i++) {
                        pathD += ` A ${arcDist} ${arcDist} 0 0 1 ${arcPoints[i].x} ${arcPoints[i].y}`;
                    }
                    
                    const arc = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                    arc.setAttribute('d', pathD);
                    arc.setAttribute('fill', 'none');
                    arc.setAttribute('stroke', 'var(--primary)');
                    arc.setAttribute('stroke-width', '2');
                    svg.appendChild(arc);
                }
                
            } else {
                // OR relation: direct lines to each child
                children.forEach(c => {
                    const start = nodeCoords[p];
                    const end = nodeCoords[c];
                    if (!start || !end) return;
                    
                    const angle = Math.atan2(end.y - start.y, end.x - start.x);
                    const startEdgeX = start.x + Math.cos(angle) * 27.5;
                    const startEdgeY = start.y + Math.sin(angle) * 27.5;
                    const endEdgeX = end.x - Math.cos(angle) * 31.5;
                    const endEdgeY = end.y - Math.sin(angle) * 31.5;
                    
                    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                    line.setAttribute('x1', startEdgeX);
                    line.setAttribute('y1', startEdgeY);
                    line.setAttribute('x2', endEdgeX);
                    line.setAttribute('y2', endEdgeY);
                    
                    line.setAttribute('stroke', 'rgba(99, 102, 241, 0.6)');
                    line.setAttribute('stroke-width', '2');
                    line.setAttribute('marker-end', 'url(#arrow-or)');
                    svg.appendChild(line);
                    
                    if (ruleLabel) {
                        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                        text.setAttribute('x', (startEdgeX + endEdgeX) / 2);
                        text.setAttribute('y', (startEdgeY + endEdgeY) / 2 - 12);
                        text.setAttribute('fill', 'var(--text-main)');
                        text.setAttribute('font-size', '14px'); // larger font
                        text.setAttribute('font-weight', 'bold');
                        text.setAttribute('text-anchor', 'middle');
                        text.textContent = ruleLabel;
                        svg.appendChild(text);
                    }
                });
            }
        });
    });
    
    // Build arrowheads
    let defs = svg.querySelector('defs');
    if (!defs) {
        defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
        
        // Primary arrow
        const markerAnd = document.createElementNS('http://www.w3.org/2000/svg', 'marker');
        markerAnd.setAttribute('id', 'arrow');
        markerAnd.setAttribute('viewBox', '0 0 10 10');
        markerAnd.setAttribute('refX', '6');
        markerAnd.setAttribute('refY', '5');
        markerAnd.setAttribute('markerWidth', '6');
        markerAnd.setAttribute('markerHeight', '6');
        markerAnd.setAttribute('orient', 'auto-start-reverse');
        const pathAnd = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        pathAnd.setAttribute('d', 'M 0 0 L 10 5 L 0 10 z');
        pathAnd.setAttribute('fill', 'var(--primary)');
        markerAnd.appendChild(pathAnd);
        defs.appendChild(markerAnd);
        
        // OR arrow
        const markerOr = document.createElementNS('http://www.w3.org/2000/svg', 'marker');
        markerOr.setAttribute('id', 'arrow-or');
        markerOr.setAttribute('viewBox', '0 0 10 10');
        markerOr.setAttribute('refX', '6');
        markerOr.setAttribute('refY', '5');
        markerOr.setAttribute('markerWidth', '6');
        markerOr.setAttribute('markerHeight', '6');
        markerOr.setAttribute('orient', 'auto-start-reverse');
        const pathOr = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        pathOr.setAttribute('d', 'M 0 0 L 10 5 L 0 10 z');
        pathOr.setAttribute('fill', 'rgba(99, 102, 241, 0.6)');
        markerOr.appendChild(pathOr);
        defs.appendChild(markerOr);
        
        svg.appendChild(defs);
    }
}

async function submitWorkspaceSolve() {
    if (interactiveState.simulationActive) return;

    const ex = interactiveExercises[interactiveState.currentExId];
    if (!ex) return;

    const selectedPredict = document.querySelector('input[name="solvability-prediction"]:checked')?.value;
    if (!selectedPredict) {
        showToast('Vui lòng dự đoán tính khả thi của Goal trước!', 'warning');
        return;
    }

    interactiveState.simulationActive = true;

    // Reset visual styles of nodes
    ex.nodes.forEach(n => {
        const el = document.getElementById(`node-${n.id}`);
        if (el) {
            el.className = 'interactive-node';
        }
    });

    const consoleLog = document.getElementById('simulation-log-list');
    const validationCard = document.getElementById('simulation-validation-card');
    const summaryBox = document.getElementById('simulation-summary-box');

    validationCard.classList.remove('hidden');
    consoleLog.innerHTML = '';
    summaryBox.classList.add('hidden');

    function logToConsole(message, type = 'info') {
        const p = document.createElement('p');
        p.style.margin = '4px 0';
        if (type === 'success') p.style.color = '#10b981';
        else if (type === 'danger') p.style.color = '#ef4444';
        else if (type === 'warning') p.style.color = '#f59e0b';
        p.innerHTML = message;
        consoleLog.appendChild(p);
        consoleLog.scrollTop = consoleLog.scrollHeight;
    }

    const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    // Evaluate step-by-step using DFS/BFS with user connections and configurations
    const visited = new Set();
    const evaluationResults = {}; // nodeId -> boolean (success/failed)

    async function evaluateNode(nodeId) {
        const el = document.getElementById(`node-${nodeId}`);
        if (el) {
            el.classList.add('node-active');
        }

        logToConsole(`&raquo; Đang kiểm tra node: <strong>${nodeId}</strong>`, 'warning');
        await sleep(1000);

        if (ex.goal.includes(nodeId)) {
            logToConsole(`✓ Node <strong>${nodeId}</strong> là Goal state. Thành công!`, 'success');
            if (el) {
                el.classList.remove('node-active');
                el.classList.add('node-success');
            }
            evaluationResults[nodeId] = true;
            return true;
        }

        const groups = interactiveState.userConnections[nodeId] || {};
        const groupIds = Object.keys(groups);
        if (groupIds.length === 0) {
            logToConsole(`✗ Node <strong>${nodeId}</strong> không có nhánh con và không phải Goal. Thất bại!`, 'danger');
            if (el) {
                el.classList.remove('node-active');
                el.classList.add('node-failed');
            }
            evaluationResults[nodeId] = false;
            return false;
        }

        let hasGroupSuccess = false;

        for (let g of groupIds) {
            const children = groups[g];
            const relation = (interactiveState.userRelations[nodeId] && interactiveState.userRelations[nodeId][g]) ? interactiveState.userRelations[nodeId][g] : 'OR';
            logToConsole(`Đang xét quan hệ <strong>${relation}</strong> của node <strong>${nodeId}</strong> (Luật ${g})...`);

            let groupSuccess = false;
            const results = [];

            if (relation === 'AND') {
                // AND: all children must succeed. Evaluate ALL children for full visual display (no pruning).
                for (let i = 0; i < children.length; i++) {
                    const child = children[i];
                    logToConsole(`Kiểm tra nhánh con <strong>${child}</strong> của AND node <strong>${nodeId}</strong> (Luật ${g})...`);
                    const success = await evaluateNode(child);
                    results.push(success);
                }
                groupSuccess = results.length === children.length && results.every(r => r === true);
                if (!groupSuccess) {
                    logToConsole(`⚡ AND (Luật ${g}): Có nhánh con thất bại → nhóm thất bại.`, 'danger');
                }
            } else {
                // OR: any child success → group succeeds. Evaluate ALL children for full visual display.
                for (let i = 0; i < children.length; i++) {
                    const child = children[i];
                    logToConsole(`Kiểm tra nhánh con <strong>${child}</strong> của OR node <strong>${nodeId}</strong> (Luật ${g})...`);
                    const success = await evaluateNode(child);
                    results.push(success);
                }
                groupSuccess = results.some(r => r === true);
                if (groupSuccess) {
                    logToConsole(`⚡ OR (Luật ${g}): Có nhánh con thành công → nhóm thành công.`, 'success');
                }
            }

            if (groupSuccess) {
                logToConsole(`✓ Nhóm luật <strong>${g}</strong> của node <strong>${nodeId}</strong> THÀNH CÔNG.`, 'success');
                hasGroupSuccess = true;
                // No break — evaluate ALL groups so all branches light up visually
            } else {
                logToConsole(`✗ Nhóm luật <strong>${g}</strong> của node <strong>${nodeId}</strong> THẤT BẠI.`, 'warning');
            }
        }

        const finalSuccess = hasGroupSuccess;
        if (el) {
            el.classList.remove('node-active');
            el.classList.add(finalSuccess ? 'node-success' : 'node-failed');
        }
        logToConsole(finalSuccess ? `✓ Node <strong>${nodeId}</strong> thành công vì có một nhóm luật thành công.` : `✗ Node <strong>${nodeId}</strong> thất bại vì toàn bộ nhóm luật đều thất bại.`, finalSuccess ? 'success' : 'danger');
        evaluationResults[nodeId] = finalSuccess;
        return finalSuccess;
    }

    const startNode = ex.initialState;
    const goalFeasible = await evaluateNode(startNode);

    // Verify structural configuration correctness
    let structureCorrect = true;
    
    const expectedFeasible = evaluateCorrectFeasibility(ex.initialState, ex.correctLinks, ex.correctRelations, ex.goal);

    // Check 1: User's drawn graph must produce the same feasibility result as the expected answer
    if (goalFeasible !== expectedFeasible) {
        structureCorrect = false;
    }

    // Check 2: For each parent node the user connected, check if the AND/OR relation matches
    // expected – but ONLY for nodes that appear in correctRelations.
    // This prevents penalizing users who drew fewer branches than expected.
    for (const p of Object.keys(interactiveState.userConnections)) {
        const expectedRel = ex.correctRelations[p];
        if (!expectedRel) continue; // node not in answer key, skip
        
        const userGroups = interactiveState.userRelations[p] || {};
        const userRels = Object.values(userGroups);
        
        if (expectedRel === 'AND') {
            // At least one group the user created for this parent must be AND
            if (!userRels.includes('AND')) {
                structureCorrect = false;
            }
        } else {
            // Expected OR: none of the groups should be AND (if user only has groups for this parent)
            if (userRels.length > 0 && userRels.every(r => r === 'AND')) {
                structureCorrect = false;
            }
        }
    }

    // Check 3: Ensure the user connected the correct children for at least the key nodes
    // Key nodes = nodes in correctLinks that are on the winning path
    const keyParents = Object.keys(ex.correctLinks);
    for (const p of keyParents) {
        const correctChildren = ex.correctLinks[p];
        const groups = interactiveState.userConnections[p] || {};
        const userChildrenSet = new Set();
        Object.keys(groups).forEach(g => groups[g].forEach(c => userChildrenSet.add(c)));
        const userChildren = Array.from(userChildrenSet);
        
        // Must contain all correct children (may have extras only if the goal is still correct)
        const missingChildren = correctChildren.filter(c => !userChildren.includes(c));
        if (missingChildren.length > 0) {
            // Missing a critical child → wrong structure
            structureCorrect = false;
        }
    }

    // Check prediction correctness (expectedFeasible already computed above in Check 1)
    const predictionIsCorrect = (selectedPredict === 'yes' && expectedFeasible) || (selectedPredict === 'no' && !expectedFeasible);

    // Render Summary box
    summaryBox.classList.remove('hidden');
    let summaryHtml = '';
    
    if (structureCorrect && predictionIsCorrect) {
        summaryBox.style.borderLeftColor = 'var(--success)';
        summaryHtml += `<h4 style="color: var(--success); margin-bottom: 8px; display: flex; align-items: center; gap: 5px;"><span class="material-icons-round">check_circle</span> Kết quả: Hoàn thành chính xác!</h4>`;
    } else {
        summaryBox.style.borderLeftColor = 'var(--danger)';
        summaryHtml += `<h4 style="color: var(--danger); margin-bottom: 8px; display: flex; align-items: center; gap: 5px;"><span class="material-icons-round">cancel</span> Kết quả: Có lỗi sai trong bài làm!</h4>`;
    }

    // Show details
    summaryHtml += `<p style="margin: 4px 0; font-size: 13.5px;">&bull; <strong>Cấu trúc & Quan hệ đồ thị:</strong> ${structureCorrect ? '<span style="color: var(--success); font-weight:700;">Chính xác</span>' : '<span style="color: var(--danger); font-weight:700;">Chưa chính xác (Kiểm tra lại liên kết hoặc AND/OR)</span>'}</p>`;
    summaryHtml += `<p style="margin: 4px 0; font-size: 13.5px;">&bull; <strong>Dự đoán khả thi:</strong> ${predictionIsCorrect ? '<span style="color: var(--success); font-weight:700;">Chính xác</span>' : '<span style="color: var(--danger); font-weight:700;">Sai</span>'}</p>`;

    summaryHtml += `<div class="divider" style="margin: 10px 0;"></div>`;
    summaryHtml += `<p style="font-weight: 700; font-size: 14px; margin-bottom: 5px;">Tóm tắt thuật toán & Lời giải:</p>`;

    if (expectedFeasible) {
        summaryHtml += `<p style="font-size: 13px; color: var(--success-dark); font-weight: 600;">✓ Goal KHẢ THI</p>`;
    } else {
        summaryHtml += `<p style="font-size: 13px; color: var(--danger-dark); font-weight: 600;">✗ Goal KHÔNG KHẢ THI</p>`;
    }

    // Dynamic explanation
    if (interactiveState.currentExId === 'ex1') {
        summaryHtml += `<p style="font-size: 13px; margin-top: 5px; color: var(--text-muted);">Giải thích: S là AND node yêu cầu cả A và B thành công. A (AND node) yêu cầu cả D và E thành công (đều là Goal). B thành công vì là Goal. Do đó S khả thi.</p>`;
    } else if (interactiveState.currentExId === 'ex2') {
        summaryHtml += `<p style="font-size: 13px; margin-top: 5px; color: var(--text-muted);">Giải thích: Nhánh B (AND node) đi đến E và F, nhưng E không phải Goal và là ngõ cụt (dead end). Khiến B thất bại. Vì S là AND node, một nhánh con (B) thất bại làm toàn bộ S thất bại.</p>`;
    } else if (interactiveState.currentExId === 'ex3') {
        summaryHtml += `<p style="font-size: 13px; margin-top: 5px; color: var(--text-muted);">Giải thích: S là OR node chỉ cần A hoặc B thành công. Nhánh B đi đến D, E, F. E dẫn đến H. D dẫn đến H. F là Goal. Toàn bộ con của B đều đạt mục tiêu, do đó B thành công, kéo theo S thành công.</p>`;
    } else {
        summaryHtml += `<p style="font-size: 13px; margin-top: 5px; color: var(--text-muted);">Giải thích: Dựa trên các quy tắc AND (yêu cầu tất cả nhánh con thành công) và OR (chỉ cần một nhánh thành công).</p>`;
    }

    summaryBox.innerHTML = summaryHtml;
    
    // Save completion stat if correct
    if (structureCorrect && predictionIsCorrect) {
        const stats = storage.loadStats('trituenhantao-ontap') || {};
        stats.interactiveCompleted = stats.interactiveCompleted || [];
        if (!stats.interactiveCompleted.includes(interactiveState.currentExId)) {
            stats.interactiveCompleted.push(interactiveState.currentExId);
            storage.saveStats('trituenhantao-ontap', stats);
            updateGlobalProgressBar();
        }
    } else {
        // Show correct graph side-by-side if structure is wrong
        if (!structureCorrect) {
            const correctCanvas = document.getElementById('correct-canvas-area');
            const userLabel = document.getElementById('user-canvas-label');
            if (correctCanvas && userLabel) {
                correctCanvas.classList.remove('hidden');
                userLabel.classList.remove('hidden');
                drawCorrectGraph();
            }
            summaryHtml += `<div style="margin-top: 15px;"><button class="btn btn-outline btn-sm" onclick="document.getElementById('btn-reset-graph').click()"><span class="material-icons-round">refresh</span> Làm lại bài này</button></div>`;
            summaryBox.innerHTML = summaryHtml; // Update again
        }
    }


    interactiveState.simulationActive = false;
}

function evaluateCorrectFeasibility(nodeId, correctLinks, correctRelations, goal) {
    if (goal.includes(nodeId)) return true;
    const children = correctLinks[nodeId] || [];
    if (children.length === 0) return false;

    const rel = correctRelations[nodeId] || 'OR';
    if (rel === 'AND') {
        return children.every(c => evaluateCorrectFeasibility(c, correctLinks, correctRelations, goal));
    } else {
        return children.some(c => evaluateCorrectFeasibility(c, correctLinks, correctRelations, goal));
    }
}

// ==========================================================================
// EXAM DISCOVERY & PARSING LOGIC
// ==========================================================================

async function scanSubjectExams(subjectId) {
    const folderMap = {
        'java': 'java-on-tap',
        'python': 'python-on-tap',
        'quocphong_hp1': 'quocphong',
        'quocphong_hp2': 'quocphong',
        'antoanthongtin-ontap': 'antoanthongtin-ontap',
        'trituenhantao-ontap': 'trituenhantao-ontap'
    };
    const folderName = folderMap[subjectId] || subjectId;
    const defaultExams = {
        'antoanthongtin-ontap': ['cauhoi-de1-attt.md', 'cauhoi-de2-attt.md'],
        'python': ['dethithu1.md']
    };
    
    let scannedFiles = [];
    try {
        const response = await fetch(`pdf/${folderName}/`);
        if (response.ok) {
            const html = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const links = Array.from(doc.querySelectorAll('a'));
            links.forEach(link => {
                const href = link.getAttribute('href') || '';
                const filename = href.split('/').pop().split('?')[0];
                if (filename.toLowerCase().endsWith('.md') && filename.toLowerCase().includes('de')) {
                    if (!scannedFiles.includes(filename)) {
                        scannedFiles.push(filename);
                    }
                }
            });
        }
    } catch (e) {
        console.warn("Could not scan directory listing dynamically. Falling back to default list.", e);
    }
    
    if (scannedFiles.length === 0) {
        scannedFiles = defaultExams[subjectId] || [];
    }
    
    return scannedFiles;
}

function findMatchingQuestion(questionText, questionsData) {
    if (!questionsData || questionsData.length === 0) return null;
    const cleanText = (txt) => txt.replace(/\s+/g, '').toLowerCase();
    const cleanQText = cleanText(questionText);
    
    for (const q of questionsData) {
        const cleanDbText = cleanText(q.question);
        if (cleanQText.includes(cleanDbText) || cleanDbText.includes(cleanQText)) {
            return q;
        }
    }
    return null;
}

function parseMarkdownFile(content, filename, dbQuestions) {
    content = content.replace(/\r\n/g, '\n');
    const isMoodle = content.includes('Đoạn văn câu hỏi') || content.includes('Câu hỏi 1Trả lời');
    
    if (isMoodle) {
        return parseMoodleFormat(content, dbQuestions);
    } else {
        return parseStandardFormat(content, dbQuestions);
    }
}

function parseMoodleFormat(content, dbQuestions) {
    const segments = content.split(/\nCâu hỏi \d+\n/);
    const qSegments = segments.slice(1);
    const parsedQuestions = [];
    
    qSegments.forEach((segment, idx) => {
        const parts = segment.split(/Câu hỏi \d+Trả lời\n/);
        if (parts.length < 2) return;
        
        const qBody = parts[0];
        const optionsBody = parts[1];
        
        const qLines = qBody.split('\n');
        const cleanedQLines = [];
        qLines.forEach(line => {
            if (line.includes('ĐúngĐạt điểm') || line.includes('SaiĐạt điểm') || line.includes('Đoạn văn câu hỏi') || line.includes('Đặt cờ')) {
                return;
            }
            cleanedQLines.push(line);
        });
        const questionText = cleanedQLines.join('\n').trim();
        
        const optBlocks = optionsBody.split(/\n([A-D])\.\n/);
        const options = [];
        for (let i = 1; i < optBlocks.length; i += 2) {
            const letter = optBlocks[i];
            const optVal = optBlocks[i+1] ? optBlocks[i+1].trim() : '';
            const cleanContent = optVal.replace(/^[A-D]\.\s*/, '').trim();
            options.push({ letter, text: cleanContent });
        }
        
        let matchedQ = findMatchingQuestion(questionText, dbQuestions);
        
        let finalOptions = options.map(o => o.text);
        if (finalOptions.length === 0) {
            finalOptions = ['A', 'B', 'C', 'D'];
        }
        
        const parsedQ = {
            id: idx + 1,
            question: questionText.trim(),
            options: finalOptions,
            correctAnswer: 'A',
            explanation: 'Chưa có giải thích cho câu hỏi này.',
            topicId: 'general',
            multiSelect: false
        };
        
        if (matchedQ) {
            parsedQ.topicId = matchedQ.topicId;
            parsedQ.explanation = matchedQ.explanation || '';
            parsedQ.multiSelect = matchedQ.multiSelect || false;
            
            const dbCorrectAnswer = matchedQ.correctAnswer;
            
            if (parsedQ.multiSelect) {
                const correctArr = (Array.isArray(dbCorrectAnswer) ? dbCorrectAnswer : [dbCorrectAnswer]).map(letter => {
                    const idx = letter.charCodeAt(0) - 65;
                    return matchedQ.options[idx];
                });
                
                const parsedCorrectLetters = [];
                options.forEach(o => {
                    if (correctArr.includes(o.text)) {
                        parsedCorrectLetters.push(o.letter);
                    }
                });
                parsedQ.correctAnswer = parsedCorrectLetters.sort();
            } else {
                const dbCorrectIndex = dbCorrectAnswer.charCodeAt(0) - 65;
                const dbCorrectText = matchedQ.options[dbCorrectIndex];
                const foundOpt = options.find(o => o.text === dbCorrectText);
                if (foundOpt) {
                    parsedQ.correctAnswer = foundOpt.letter;
                } else {
                    parsedQ.correctAnswer = 'A';
                }
            }
        }
        
        parsedQuestions.push(parsedQ);
    });
    
    return parsedQuestions;
}

function parseStandardFormat(content, dbQuestions) {
    const lines = content.split('\n');
    const answersMap = {};
    
    const ansRegex = /^Q(\d+)\s*:\s*([A-E\s,và]+)\s*-\s*(.*)$/i;
    lines.forEach(line => {
        const match = line.trim().match(ansRegex);
        if (match) {
            const qNum = parseInt(match[1]);
            const ansStr = match[2];
            const explanation = match[3].trim();
            
            const answers = [];
            const letters = ansStr.match(/[A-E]/gi);
            if (letters) {
                letters.forEach(l => answers.push(l.toUpperCase()));
            }
            answersMap[qNum] = { answers, explanation };
        }
    });
    
    const questions = [];
    let currentQuestion = null;
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        
        const qMatch = line.match(/^Q(\d+)\s*$/i);
        if (qMatch) {
            if (currentQuestion) {
                questions.push(currentQuestion);
            }
            const qNum = parseInt(qMatch[1]);
            currentQuestion = {
                id: qNum,
                question: '',
                options: [],
                correctAnswer: [],
                explanation: '',
                topicId: 'general',
                multiSelect: false
            };
            continue;
        }
        
        if (!currentQuestion) continue;
        
        const optMatch = line.match(/^([A-E])\.\s*(.*)$/i);
        if (optMatch) {
            const text = optMatch[2].trim();
            currentQuestion.options.push(text);
            continue;
        }
        
        if (line.includes('Giải thích:')) {
            const expText = line.substring(line.indexOf('Giải thích:') + 11).trim();
            currentQuestion.explanation = expText.replace(/^\*\*|\*\*$/g, '').trim();
            continue;
        }
        
        if (line !== '' && !line.startsWith('---')) {
            if (currentQuestion.question) {
                currentQuestion.question += '\n' + line;
            } else {
                currentQuestion.question = line;
            }
        }
    }
    
    if (currentQuestion) {
        questions.push(currentQuestion);
    }
    
    questions.forEach(q => {
        const keyInfo = answersMap[q.id];
        if (keyInfo) {
            q.correctAnswer = keyInfo.answers;
            if (q.correctAnswer.length > 1) {
                q.multiSelect = true;
            } else if (q.correctAnswer.length === 1) {
                q.correctAnswer = q.correctAnswer[0];
            }
            
            if (!q.explanation) {
                q.explanation = keyInfo.explanation;
            }
        }
        
        const matchedQ = findMatchingQuestion(q.question, dbQuestions);
        if (matchedQ) {
            q.topicId = matchedQ.topicId;
        }
        
        q.question = q.question.trim();
        q.explanation = q.explanation.trim();
    });
    
    return questions;
}

async function startMarkdownExam(filename) {
    const folderMap = {
        'java': 'java-on-tap',
        'python': 'python-on-tap',
        'quocphong_hp1': 'quocphong',
        'quocphong_hp2': 'quocphong',
        'antoanthongtin-ontap': 'antoanthongtin-ontap',
        'trituenhantao-ontap': 'trituenhantao-ontap'
    };
    const folderName = folderMap[state.currentSubjectId] || state.currentSubjectId;
    
    try {
        const res = await fetch(`pdf/${folderName}/${filename}?t=${Date.now()}`);
        if (!res.ok) throw new Error("Không thể tải file đề thi.");
        
        const markdown = await res.text();
        const questions = parseMarkdownFile(markdown, filename, state.questionsData);
        
        if (questions.length === 0) {
            showToast("Không tìm thấy câu hỏi nào trong file đề thi!", "warning");
            return;
        }
        
        startMockExamWithQuestions(questions, `Đề thi: ${filename.replace('.md', '')}`);
    } catch (e) {
        console.error("Lỗi khi tải/phân tích đề thi Markdown:", e);
        showToast("Lỗi tải đề thi Markdown!", "danger");
    }
}

function startPresetExam(examId) {
    const preset = state.presetExams.find(e => e.id === examId);
    if (!preset) {
        showToast("Không tìm thấy đề thi mẫu!", "danger");
        return;
    }
    
    startMockExamWithQuestions(preset.questions, preset.name);
}

function startMockExamWithQuestions(questions, examName) {
    const size = questions.length;
    const timers = { 20: 25*60, 30: 40*60, 50: 60*60, 100: 120*60 };
    const durationSeconds = timers[size] || 55*60;
    
    state.mock.questions = questions;
    state.mock.active = true;
    state.mock.currentIndex = 0;
    state.mock.userAnswers = {};
    state.mock.startTime = new Date();
    
    state.mock.timer = durationSeconds;
    state.mock.totalTime = durationSeconds;
    
    document.getElementById('mock-setup-card').classList.add('hidden');
    document.getElementById('mock-exam-workspace-container').classList.remove('hidden');
    
    renderMockQuestionsList();
    startMockTimer();
    renderMockQuestionMap();
    
    window.location.hash = '#mock-test';
    showToast(`Đã bắt đầu bài thi: ${examName}`, 'success');
}

// Expose functions globally for onclick triggers
window.startMarkdownExam = startMarkdownExam;
window.startPresetExam = startPresetExam;
window.scanSubjectExams = scanSubjectExams;
window.startMockExamWithQuestions = startMockExamWithQuestions;



