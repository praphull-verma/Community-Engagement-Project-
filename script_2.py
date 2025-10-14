# Create the JavaScript file with interactive functionality
js_content = '''// Career data for different categories
const careerData = {
    engineering: {
        title: "Core Engineering Careers",
        icon: "⚙️",
        description: "Traditional engineering roles with modern technology integration",
        careers: [
            {
                title: "Software Developer",
                skills: ["Programming", "Problem Solving", "System Design"],
                salary: "₹6-25 LPA",
                growth: "Excellent",
                description: "Build applications, websites, and software systems"
            },
            {
                title: "Data Engineer",
                skills: ["Python/SQL", "Big Data", "Cloud Platforms"],
                salary: "₹8-30 LPA",
                growth: "High Demand",
                description: "Design and maintain data pipelines and analytics systems"
            },
            {
                title: "Mechanical Engineer",
                skills: ["CAD Design", "Manufacturing", "Project Management"],
                salary: "₹5-20 LPA",
                growth: "Stable",
                description: "Design machines, engines, and mechanical systems"
            },
            {
                title: "Civil Engineer",
                skills: ["Structural Design", "Project Planning", "AutoCAD"],
                salary: "₹4-18 LPA",
                growth: "Infrastructure Boom",
                description: "Plan and oversee construction projects and infrastructure"
            }
        ]
    },
    
    government: {
        title: "Government & Public Sector",
        icon: "🏛️",
        description: "Serve the nation through prestigious government organizations",
        careers: [
            {
                title: "Indian Engineering Services (IES)",
                skills: ["Technical Knowledge", "Leadership", "Public Administration"],
                salary: "₹56,100-2,25,000 (Pay Scale)",
                growth: "Prestigious Career",
                description: "Central government engineering positions in various ministries"
            },
            {
                title: "PSU Engineer (ONGC, NTPC, BHEL)",
                skills: ["Domain Expertise", "Project Management", "Operations"],
                salary: "₹8-25 LPA",
                growth: "Job Security",
                description: "Work in public sector undertakings in core industries"
            },
            {
                title: "ISRO Scientist",
                skills: ["Aerospace Engineering", "Research", "Innovation"],
                salary: "₹6-20 LPA",
                growth: "Space Technology",
                description: "Contribute to India's space program and satellite technology"
            },
            {
                title: "Railways Engineering",
                skills: ["Railway Systems", "Safety Protocols", "Maintenance"],
                salary: "₹5-18 LPA",
                growth: "Infrastructure Development",
                description: "Maintain and develop India's vast railway network"
            }
        ]
    },
    
    creative: {
        title: "Creative & Design Careers",
        icon: "🎨",
        description: "Express creativity through technology and artistic innovation",
        careers: [
            {
                title: "UI/UX Designer",
                skills: ["Design Thinking", "Prototyping", "User Research"],
                salary: "₹4-20 LPA",
                growth: "High Demand",
                description: "Create intuitive and beautiful digital experiences"
            },
            {
                title: "Game Developer",
                skills: ["Programming", "3D Modeling", "Game Engines"],
                salary: "₹5-25 LPA",
                growth: "Gaming Industry Boom",
                description: "Develop engaging games and interactive entertainment"
            },
            {
                title: "Motion Graphics Artist",
                skills: ["After Effects", "3D Animation", "Visual Storytelling"],
                salary: "₹3-15 LPA",
                growth: "Digital Content Growth",
                description: "Create animated content for films, ads, and digital media"
            },
            {
                title: "Product Designer",
                skills: ["Industrial Design", "CAD", "User-Centered Design"],
                salary: "₹6-22 LPA",
                growth: "Innovation Focus",
                description: "Design physical products from concept to manufacturing"
            }
        ]
    },
    
    communication: {
        title: "Communication & Media",
        icon: "💬",
        description: "Bridge technology and people through effective communication",
        careers: [
            {
                title: "Technical Writer",
                skills: ["Writing", "Technical Knowledge", "Documentation"],
                salary: "₹4-18 LPA",
                growth: "Tech Documentation Need",
                description: "Create user manuals, API docs, and technical content"
            },
            {
                title: "Science Communicator",
                skills: ["Science Knowledge", "Public Speaking", "Content Creation"],
                salary: "₹3-12 LPA",
                growth: "Science Awareness",
                description: "Make complex scientific concepts accessible to the public"
            },
            {
                title: "EdTech Content Creator",
                skills: ["Subject Expertise", "Video Production", "Pedagogy"],
                salary: "₹4-20 LPA",
                growth: "Online Education Boom",
                description: "Develop educational content and online courses"
            },
            {
                title: "Technology Journalist",
                skills: ["Writing", "Tech Understanding", "Research"],
                salary: "₹3-15 LPA",
                growth: "Tech Media Growth",
                description: "Report on technology trends and innovations"
            }
        ]
    },
    
    business: {
        title: "Business & Management",
        icon: "💼",
        description: "Lead teams and drive business innovation with technical expertise",
        careers: [
            {
                title: "Product Manager",
                skills: ["Strategy", "Analytics", "Technical Understanding"],
                salary: "₹8-35 LPA",
                growth: "Very High Demand",
                description: "Guide product development from idea to market success"
            },
            {
                title: "Business Analyst",
                skills: ["Data Analysis", "Process Optimization", "Communication"],
                salary: "₹5-20 LPA",
                growth: "Data-Driven Decisions",
                description: "Analyze business processes and recommend improvements"
            },
            {
                title: "Operations Manager",
                skills: ["Process Management", "Leadership", "Problem Solving"],
                salary: "₹6-25 LPA",
                growth: "Operational Efficiency",
                description: "Optimize business operations and manage teams"
            },
            {
                title: "Management Consultant",
                skills: ["Problem Solving", "Strategy", "Client Management"],
                salary: "₹8-30 LPA",
                growth: "Business Transformation",
                description: "Help organizations solve complex business challenges"
            }
        ]
    },
    
    finance: {
        title: "Finance & Analytics",
        icon: "💰",
        description: "Apply technical and analytical skills to financial markets",
        careers: [
            {
                title: "Investment Banking Analyst",
                skills: ["Financial Modeling", "Valuation", "Market Analysis"],
                salary: "₹10-40 LPA",
                growth: "High Rewards",
                description: "Analyze investments and support financial transactions"
            },
            {
                title: "Quantitative Analyst",
                skills: ["Mathematics", "Programming", "Statistical Modeling"],
                salary: "₹12-45 LPA",
                growth: "Algorithmic Trading",
                description: "Develop mathematical models for financial markets"
            },
            {
                title: "Risk Analyst",
                skills: ["Risk Assessment", "Data Analysis", "Compliance"],
                salary: "₹6-22 LPA",
                growth: "Regulatory Requirements",
                description: "Assess and mitigate financial and operational risks"
            },
            {
                title: "FinTech Developer",
                skills: ["Programming", "Financial Systems", "Security"],
                salary: "₹8-30 LPA",
                growth: "Digital Finance Revolution",
                description: "Build technology solutions for financial services"
            }
        ]
    },
    
    social: {
        title: "Social Impact & Policy",
        icon: "🌱",
        description: "Create sustainable solutions and positive social change",
        careers: [
            {
                title: "Policy Analyst",
                skills: ["Research", "Policy Analysis", "Communication"],
                salary: "₹4-15 LPA",
                growth: "Governance Focus",
                description: "Research and analyze public policies and their impact"
            },
            {
                title: "Sustainability Consultant",
                skills: ["Environmental Science", "Project Management", "Analytics"],
                salary: "₹5-18 LPA",
                growth: "Climate Action",
                description: "Help organizations implement sustainable practices"
            },
            {
                title: "Social Entrepreneur",
                skills: ["Innovation", "Leadership", "Social Impact"],
                salary: "Variable (Impact-based)",
                growth: "Social Innovation",
                description: "Build ventures that solve social and environmental problems"
            },
            {
                title: "Development Sector Program Manager",
                skills: ["Project Management", "Community Engagement", "Monitoring"],
                salary: "₹4-16 LPA",
                growth: "Rural Development",
                description: "Implement programs for rural and community development"
            }
        ]
    },
    
    startup: {
        title: "Entrepreneurship & Startups",
        icon: "🚀",
        description: "Build innovative ventures and disruptive solutions",
        careers: [
            {
                title: "Tech Startup Founder",
                skills: ["Vision", "Leadership", "Technical Skills", "Fundraising"],
                salary: "Equity-based (Unlimited potential)",
                growth: "Innovation Economy",
                description: "Build and scale technology companies from ground up"
            },
            {
                title: "Freelance Consultant",
                skills: ["Expertise", "Client Management", "Business Development"],
                salary: "₹500-5000 per hour",
                growth: "Gig Economy",
                description: "Provide specialized consulting services to businesses"
            },
            {
                title: "E-commerce Entrepreneur",
                skills: ["Digital Marketing", "Supply Chain", "Customer Service"],
                salary: "Variable (Business dependent)",
                growth: "Digital Commerce",
                description: "Build online retail and service businesses"
            },
            {
                title: "SaaS Product Builder",
                skills: ["Software Development", "Product Strategy", "Marketing"],
                salary: "Subscription-based revenue",
                growth: "Software as Service",
                description: "Create software products that serve businesses globally"
            }
        ]
    }
};

// Quiz questions and scoring
const quizQuestions = [
    {
        question: "What type of work environment excites you most?",
        options: [
            { text: "Fast-paced startup with cutting-edge technology", categories: ["startup", "engineering"] },
            { text: "Stable government organization serving the public", categories: ["government", "social"] },
            { text: "Creative agency or design studio", categories: ["creative", "communication"] },
            { text: "Corporate office managing teams and projects", categories: ["business", "finance"] }
        ]
    },
    {
        question: "Which of these activities do you find most engaging?",
        options: [
            { text: "Solving complex technical problems", categories: ["engineering", "finance"] },
            { text: "Creating visual designs or content", categories: ["creative", "communication"] },
            { text: "Leading teams and making strategic decisions", categories: ["business", "startup"] },
            { text: "Contributing to social causes and policy", categories: ["social", "government"] }
        ]
    },
    {
        question: "What motivates you most in a career?",
        options: [
            { text: "High financial rewards and growth potential", categories: ["finance", "startup"] },
            { text: "Job security and prestigious recognition", categories: ["government", "engineering"] },
            { text: "Creative freedom and artistic expression", categories: ["creative", "communication"] },
            { text: "Making a positive impact on society", categories: ["social", "government"] }
        ]
    },
    {
        question: "How do you prefer to work?",
        options: [
            { text: "Independently with flexible schedules", categories: ["startup", "creative"] },
            { text: "In structured teams with clear processes", categories: ["government", "engineering"] },
            { text: "Collaboratively on innovative projects", categories: ["business", "communication"] },
            { text: "With data and analytical challenges", categories: ["finance", "engineering"] }
        ]
    },
    {
        question: "Which skill would you most like to develop further?",
        options: [
            { text: "Advanced programming and technical skills", categories: ["engineering", "startup"] },
            { text: "Leadership and people management", categories: ["business", "government"] },
            { text: "Creative and design thinking", categories: ["creative", "communication"] },
            { text: "Financial analysis and market understanding", categories: ["finance", "social"] }
        ]
    }
];

let currentQuestionIndex = 0;
let quizScores = {};
let selectedAnswers = [];

// Initialize the website
document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    initializeQuiz();
    setupSearch();
    setupMobileMenu();
});

function initializeEventListeners() {
    // Career card click handlers
    document.querySelectorAll('.career-card').forEach(card => {
        card.addEventListener('click', function() {
            const category = this.getAttribute('data-category');
            openCareerModal(category);
        });
    });

    // Modal close handlers
    const modal = document.getElementById('careerModal');
    const closeBtn = document.querySelector('.close');
    
    closeBtn.addEventListener('click', closeModal);
    window.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });
}

function openCareerModal(category) {
    const modal = document.getElementById('careerModal');
    const modalContent = document.getElementById('modalContent');
    const data = careerData[category];
    
    if (!data) return;
    
    let html = `
        <h2>${data.icon} ${data.title}</h2>
        <p class="modal-description">${data.description}</p>
        <div class="careers-list">
    `;
    
    data.careers.forEach(career => {
        html += `
            <div class="career-detail">
                <h3>${career.title}</h3>
                <p>${career.description}</p>
                <div class="career-info">
                    <div class="info-item">
                        <strong>Key Skills:</strong> ${career.skills.join(', ')}
                    </div>
                    <div class="info-item">
                        <strong>Salary Range:</strong> ${career.salary}
                    </div>
                    <div class="info-item">
                        <strong>Growth Outlook:</strong> ${career.growth}
                    </div>
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    modalContent.innerHTML = html;
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('careerModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function initializeQuiz() {
    // Initialize quiz scores
    Object.keys(careerData).forEach(category => {
        quizScores[category] = 0;
    });
    
    displayQuestion();
    updateQuizNavigation();
}

function displayQuestion() {
    const quizContent = document.getElementById('quizContent');
    const question = quizQuestions[currentQuestionIndex];
    
    if (!question) {
        showQuizResults();
        return;
    }
    
    let html = `
        <div class="quiz-question">
            <h3>${question.question}</h3>
            <div class="quiz-options">
    `;
    
    question.options.forEach((option, index) => {
        const isSelected = selectedAnswers[currentQuestionIndex] === index;
        html += `
            <div class="quiz-option ${isSelected ? 'selected' : ''}" 
                 onclick="selectOption(${index})" 
                 data-option="${index}">
                ${option.text}
            </div>
        `;
    });
    
    html += '</div></div>';
    quizContent.innerHTML = html;
    
    // Update progress
    const progressFill = document.getElementById('progressFill');
    const progress = ((currentQuestionIndex + 1) / quizQuestions.length) * 100;
    progressFill.style.width = progress + '%';
    
    document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
    document.getElementById('totalQuestions').textContent = quizQuestions.length;
}

function selectOption(optionIndex) {
    // Remove previous selection
    document.querySelectorAll('.quiz-option').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Add selection to clicked option
    const selectedOption = document.querySelector(`[data-option="${optionIndex}"]`);
    selectedOption.classList.add('selected');
    
    // Store the selection
    selectedAnswers[currentQuestionIndex] = optionIndex;
    
    // Update scores
    const question = quizQuestions[currentQuestionIndex];
    const selectedChoice = question.options[optionIndex];
    
    selectedChoice.categories.forEach(category => {
        quizScores[category] += 1;
    });
}

function nextQuestion() {
    if (selectedAnswers[currentQuestionIndex] === undefined) {
        alert('Please select an answer before proceeding.');
        return;
    }
    
    currentQuestionIndex++;
    
    if (currentQuestionIndex >= quizQuestions.length) {
        showQuizResults();
    } else {
        displayQuestion();
        updateQuizNavigation();
    }
}

function prevQuestion() {
    if (currentQuestionIndex > 0) {
        // Remove scores from current question before going back
        if (selectedAnswers[currentQuestionIndex] !== undefined) {
            const question = quizQuestions[currentQuestionIndex];
            const selectedChoice = question.options[selectedAnswers[currentQuestionIndex]];
            selectedChoice.categories.forEach(category => {
                quizScores[category] -= 1;
            });
        }
        
        currentQuestionIndex--;
        displayQuestion();
        updateQuizNavigation();
    }
}

function updateQuizNavigation() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    
    prevBtn.style.display = currentQuestionIndex > 0 ? 'block' : 'none';
    nextBtn.textContent = currentQuestionIndex === quizQuestions.length - 1 ? 'Get Results' : 'Next';
    
    // Add event listeners
    nextBtn.onclick = nextQuestion;
    prevBtn.onclick = prevQuestion;
}

function showQuizResults() {
    // Calculate top 3 career matches
    const sortedScores = Object.entries(quizScores)
        .sort(([,a], [,b]) => b - a)
        .slice(0, 3);
    
    const quizContent = document.getElementById('quizContent');
    const quizNavigation = document.querySelector('.quiz-navigation');
    const quizResults = document.getElementById('quizResults');
    const resultsCards = document.getElementById('resultsCards');
    
    // Hide question content and navigation
    quizContent.style.display = 'none';
    quizNavigation.style.display = 'none';
    
    // Show results
    let html = '';
    sortedScores.forEach(([category, score], index) => {
        const data = careerData[category];
        const percentage = Math.round((score / quizQuestions.length) * 100);
        
        html += `
            <div class="result-card" onclick="openCareerModal('${category}')">
                <div class="result-header">
                    <span class="result-icon">${data.icon}</span>
                    <div class="result-info">
                        <h3>${data.title}</h3>
                        <div class="match-percentage">${percentage}% Match</div>
                    </div>
                </div>
                <p>${data.description}</p>
                <div class="sample-careers">
                    <strong>Sample Careers:</strong> ${data.careers.slice(0, 2).map(c => c.title).join(', ')}
                </div>
            </div>
        `;
    });
    
    resultsCards.innerHTML = html;
    quizResults.style.display = 'block';
}

function setupSearch() {
    const searchInput = document.getElementById('careerSearch');
    const searchBtn = document.querySelector('.search-btn');
    
    function performSearch() {
        const query = searchInput.value.toLowerCase().trim();
        if (!query) return;
        
        // Simple search logic
        let matchedCategory = null;
        
        // Search through career categories
        Object.entries(careerData).forEach(([category, data]) => {
            const searchText = (data.title + ' ' + data.description + ' ' + 
                              data.careers.map(c => c.title + ' ' + c.description).join(' ')).toLowerCase();
            
            if (searchText.includes(query) && !matchedCategory) {
                matchedCategory = category;
            }
        });
        
        if (matchedCategory) {
            openCareerModal(matchedCategory);
        } else {
            // Scroll to careers section if no specific match
            scrollToSection('careers');
        }
        
        searchInput.value = '';
    }
    
    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

function setupMobileMenu() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    hamburger.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        this.classList.toggle('active');
    });
    
    // Close menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });
}

function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        const navHeight = document.querySelector('.navbar').offsetHeight;
        const sectionTop = section.offsetTop - navHeight;
        
        window.scrollTo({
            top: sectionTop,
            behavior: 'smooth'
        });
    }
}

// Add smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        scrollToSection(targetId);
    });
});

// Add navbar background on scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
    }
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.classList.add('loading');
});'''

# Save JavaScript file
with open("script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("JavaScript file created successfully!")