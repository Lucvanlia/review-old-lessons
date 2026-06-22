/**
 * EduPrep.vn - Main JavaScript Application Logic
 * Pure Vanilla JavaScript (No Frameworks)
 */

// Global Application State
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
        const response = await fetch('data/subjects.json');
        if (!response.ok) throw new Error('Không thể tải tệp subjects.json');
        state.subjects = await response.json();
        
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

    const btnSubmitMock = document.getElementById('btn-submit-mock');
    if (btnSubmitMock) {
        btnSubmitMock.addEventListener('click', () => submitMockExam(false));
    }

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
}

async function selectSubject(subjectId) {
    state.currentSubjectId = subjectId;
    state.currentSubject = state.subjects.find(s => s.id === subjectId);
    localStorage.setItem(storage.getActiveSubjectKey(), subjectId);
    
    // Update Sidebar dropdown selection value
    const dropdown = document.getElementById('sidebar-subject-select');
    if (dropdown) dropdown.value = subjectId;
    
    // Load data files for this subject
    try {
        const knowledgeRes = await fetch(`data/${subjectId}/knowledge.json`);
        const questionsRes = await fetch(`data/${subjectId}/questions.json`);
        
        if (!knowledgeRes.ok || !questionsRes.ok) {
            throw new Error('Không thể tải các tệp tin dữ liệu môn học');
        }
        
        state.knowledgeData = await knowledgeRes.json();
        state.questionsData = await questionsRes.json();
        
        // Load preset exams if available
        try {
            const presetRes = await fetch(`data/${subjectId}/preset_exams.json`);
            if (presetRes.ok) {
                state.presetExams = await presetRes.json();
            } else {
                state.presetExams = [];
            }
        } catch (e) {
            console.warn(`Không tìm thấy preset_exams.json cho môn học ${subjectId}:`, e);
            state.presetExams = [];
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
    const container = document.getElementById('subject-cards-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    state.subjects.forEach(subject => {
        const card = document.createElement('div');
        card.className = `subject-card ${subject.id === state.currentSubjectId ? 'active' : ''}`;
        
        // Determine counts for statistics (we mock if not current, or fetch dynamically if possible)
        // For simplicity, if it's current subject we display exact lengths. 
        // For other subjects, we read placeholders or show standard count.
        const isCurrent = subject.id === state.currentSubjectId;
        const topicCount = isCurrent ? state.knowledgeData.length : 19; // Placeholder estimation for network
        const questCount = isCurrent ? state.questionsData.length : 26; // Placeholder estimation for network
        
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
                    ${isCurrent ? 'Bắt đầu học ngay' : 'Chọn môn học'}
                </button>
            </div>
        `;
        
        card.addEventListener('click', async () => {
            if (!isCurrent) {
                await selectSubject(subject.id);
            }
            window.location.hash = '#knowledge';
        });
        
        container.appendChild(card);
    });
}

// ==========================================================================
// 2. KNOWLEDGE PANEL RENDER (Notes + Markdown style presentation)
// ==========================================================================
function renderKnowledgeScreen() {
    const topicListEl = document.getElementById('knowledge-topic-list');
    const detailViewEl = document.getElementById('knowledge-detail-view');
    if (!topicListEl || !detailViewEl) return;
    
    // Clear list
    topicListEl.innerHTML = '';
    
    if (state.knowledgeData.length === 0) {
        topicListEl.innerHTML = '<div class="empty-list-info">Không có chủ đề nào.</div>';
        detailViewEl.innerHTML = '<div class="empty-state"><h3>Không có dữ liệu</h3></div>';
        return;
    }
    
    const readList = storage.loadReadTopics(state.currentSubjectId);
    
    // Render sidebar topic items
    state.knowledgeData.forEach(topic => {
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
            renderKnowledgeScreen(); // Redraw layout to update active state
        });
        
        topicListEl.appendChild(item);
    });
    
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
    
    detailViewEl.innerHTML = `
        <div class="detail-header">
            <div class="topic-label-wrap">
                <span class="badge">Chủ đề học tập</span>
                <h2 class="detail-title">${activeTopic.title}</h2>
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
    document.getElementById('quiz-question-text').textContent = q.question;
    
    // Render options cards
    const optionsContainer = document.getElementById('quiz-options-container');
    optionsContainer.innerHTML = '';
    
    const optionBadges = ['A', 'B', 'C', 'D'];
    q.options.forEach((opt, idx) => {
        const card = document.createElement('div');
        card.className = 'option-card';
        card.dataset.index = idx;
        card.dataset.letter = optionBadges[idx];
        
        card.innerHTML = `
            <div class="option-badge">${optionBadges[idx]}</div>
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
            explanationText.textContent = currentQuestion.explanation;
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
    
    const display = document.getElementById('mock-timer-text');
    const updateDisplay = () => {
        const mins = Math.floor(state.mock.timer / 60);
        const secs = state.mock.timer % 60;
        display.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        
        // Add danger blink on low time (under 1 minute)
        const timerContainer = document.getElementById('mock-timer');
        if (state.mock.timer <= 60) {
            timerContainer.style.background = '#fee2e2';
            timerContainer.style.color = '#ef4444';
        } else {
            timerContainer.style.background = '';
            timerContainer.style.color = '';
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

function renderMockQuestion() {
    const q = state.mock.questions[state.mock.currentIndex];
    
    document.getElementById('mock-current-idx').textContent = state.mock.currentIndex + 1;
    document.getElementById('mock-question-text').textContent = q.question;
    
    const optionsContainer = document.getElementById('mock-options-container');
    optionsContainer.innerHTML = '';
    
    const optionBadges = ['A', 'B', 'C', 'D'];
    const savedAnswer = state.mock.userAnswers[state.mock.currentIndex];
    
    q.options.forEach((opt, idx) => {
        const card = document.createElement('div');
        const letter = optionBadges[idx];
        const isSelected = savedAnswer === letter;
        
        card.className = `option-card ${isSelected ? 'selected' : ''}`;
        
        card.innerHTML = `
            <div class="option-badge">${letter}</div>
            <div class="option-text">${opt}</div>
        `;
        
        card.addEventListener('click', () => selectMockOption(letter));
        optionsContainer.appendChild(card);
    });
    
    // Toggle Prev/Next buttons
    document.getElementById('btn-mock-prev').disabled = state.mock.currentIndex === 0;
    
    const nextBtn = document.getElementById('btn-mock-next');
    if (state.mock.currentIndex === state.mock.questions.length - 1) {
        nextBtn.innerHTML = `Cuối cùng <span class="material-icons-round">vertical_align_bottom</span>`;
        nextBtn.disabled = true;
    } else {
        nextBtn.innerHTML = `Kế tiếp <span class="material-icons-round">chevron_right</span>`;
        nextBtn.disabled = false;
    }
    
    updateMockQuestionMapStatus();
}

function selectMockOption(letter) {
    state.mock.userAnswers[state.mock.currentIndex] = letter;
    
    // Re-render only options cards to display selected state
    const allCards = document.querySelectorAll('#mock-options-container .option-card');
    const optionBadges = ['A', 'B', 'C', 'D'];
    
    allCards.forEach((card, idx) => {
        if (optionBadges[idx] === letter) {
            card.classList.add('selected');
        } else {
            card.classList.remove('selected');
        }
    });
    
    updateMockQuestionMapStatus();
}

function navigateMockQuestion(direction) {
    const targetIdx = state.mock.currentIndex + direction;
    if (targetIdx >= 0 && targetIdx < state.mock.questions.length) {
        state.mock.currentIndex = targetIdx;
        renderMockQuestion();
    }
}

function jumpToMockQuestion(idx) {
    if (idx >= 0 && idx < state.mock.questions.length) {
        state.mock.currentIndex = idx;
        renderMockQuestion();
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
        const userAns = state.mock.userAnswers[idx] || '';
        finalAnswersArray.push(userAns);
        
        const isCorrect = userAns === q.correctAnswer;
        if (isCorrect) correctCount++;
        
        // Save statistics for analysis
        if (userAns) {
            updateAnswerStatistics(q.topicId, isCorrect);
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
    
    // Render review items (Only show wrong or unchecked questions)
    const wrongSection = document.getElementById('wrong-questions-section');
    const wrongListContainer = document.getElementById('wrong-questions-list-container');
    
    wrongListContainer.innerHTML = '';
    let wrongCount = 0;
    
    questions.forEach((q, idx) => {
        const userAns = userAnswers[idx] || 'Chưa trả lời';
        const correctAns = q.correctAnswer;
        
        if (userAns !== correctAns) {
            wrongCount++;
            const item = document.createElement('div');
            item.className = 'review-item';
            
            // Fetch option contents
            const optionBadges = ['A', 'B', 'C', 'D'];
            const userAnsText = q.options[optionBadges.indexOf(userAns)] || userAns;
            const correctAnsText = q.options[optionBadges.indexOf(correctAns)] || '';
            
            item.innerHTML = `
                <div class="review-q-text">Câu ${idx + 1}: ${q.question}</div>
                <div class="review-answers">
                    <div class="review-user-ans">
                        <span class="material-icons-round" style="font-size:16px">cancel</span>
                        Đáp án của bạn: ${userAns} - ${userAnsText}
                    </div>
                    <div class="review-correct-ans">
                        <span class="material-icons-round" style="font-size:16px">check_circle</span>
                        Đáp án đúng: ${correctAns} - ${correctAnsText}
                    </div>
                </div>
                ${q.explanation ? `<div class="review-exp"><strong>Giải thích:</strong> ${q.explanation}</div>` : ''}
            `;
            
            wrongListContainer.appendChild(item);
        }
    });
    
    if (wrongCount > 0) {
        wrongSection.classList.remove('hidden');
    } else {
        wrongSection.classList.add('hidden');
    }
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
