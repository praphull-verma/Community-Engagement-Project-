# Create the CSS file with modern styling and animations
css_content = '''/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    line-height: 1.6;
    color: #333;
    overflow-x: hidden;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    z-index: 1000;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
}

.nav-logo {
    display: flex;
    align-items: center;
    font-size: 24px;
    font-weight: 700;
    color: #2c5aa0;
}

.nav-logo i {
    margin-right: 10px;
    font-size: 28px;
    color: #ff6b35;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 30px;
}

.nav-link {
    text-decoration: none;
    color: #333;
    font-weight: 500;
    position: relative;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: #2c5aa0;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(45deg, #2c5aa0, #ff6b35);
    transition: width 0.3s ease;
}

.nav-link:hover::after {
    width: 100%;
}

.hamburger {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.bar {
    width: 25px;
    height: 3px;
    background: #333;
    margin: 3px 0;
    transition: 0.3s;
}

/* Hero Section */
.hero {
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
    opacity: 0.3;
}

.hero-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: center;
    position: relative;
    z-index: 2;
}

.hero-content {
    color: white;
}

.hero-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.2;
    animation: slideInLeft 1s ease-out;
}

.hero-subtitle {
    font-size: 1.2rem;
    margin-bottom: 30px;
    opacity: 0.9;
    animation: slideInLeft 1s ease-out 0.2s both;
}

.search-container {
    position: relative;
    margin-bottom: 30px;
    animation: slideInLeft 1s ease-out 0.4s both;
}

.search-input {
    width: 100%;
    padding: 15px 50px 15px 20px;
    border: none;
    border-radius: 50px;
    font-size: 16px;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.search-input:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.3);
    background: white;
}

.search-btn {
    position: absolute;
    right: 5px;
    top: 5px;
    bottom: 5px;
    background: linear-gradient(45deg, #ff6b35, #f7931e);
    border: none;
    border-radius: 50px;
    width: 40px;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
}

.search-btn:hover {
    transform: scale(1.05);
}

.cta-buttons {
    display: flex;
    gap: 20px;
    animation: slideInLeft 1s ease-out 0.6s both;
}

.btn {
    padding: 15px 30px;
    border: none;
    border-radius: 50px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
}

.btn-primary {
    background: linear-gradient(45deg, #ff6b35, #f7931e);
    color: white;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(255, 107, 53, 0.3);
}

.btn-secondary {
    background: transparent;
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.6);
}

/* Floating Icons Animation */
.hero-visual {
    position: relative;
    height: 400px;
}

.floating-icons {
    position: absolute;
    width: 100%;
    height: 100%;
}

.icon-item {
    position: absolute;
    width: 60px;
    height: 60px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: white;
    animation: float 3s ease-in-out infinite;
    animation-delay: var(--delay);
}

.icon-item:nth-child(1) { top: 10%; left: 20%; }
.icon-item:nth-child(2) { top: 30%; right: 10%; }
.icon-item:nth-child(3) { top: 60%; left: 10%; }
.icon-item:nth-child(4) { bottom: 20%; right: 30%; }
.icon-item:nth-child(5) { top: 50%; left: 50%; }

@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}

/* Career Cards Section */
.careers-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.section-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 20px;
    color: #2c5aa0;
}

.section-subtitle {
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 60px;
    color: #666;
}

.careers-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    margin-top: 50px;
}

.career-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.career-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    transition: left 0.5s ease;
}

.career-card:hover::before {
    left: 100%;
}

.career-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.card-icon {
    font-size: 3rem;
    margin-bottom: 20px;
    display: block;
}

.career-card h3 {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 15px;
    color: #2c5aa0;
}

.career-card p {
    color: #666;
    margin-bottom: 20px;
    line-height: 1.6;
}

.card-stats {
    display: flex;
    gap: 15px;
}

.stat {
    background: linear-gradient(45deg, #ff6b35, #f7931e);
    color: white;
    padding: 5px 12px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 500;
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
}

.modal-content {
    background-color: white;
    margin: 5% auto;
    padding: 30px;
    border-radius: 20px;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
    animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    position: absolute;
    right: 20px;
    top: 15px;
}

.close:hover {
    color: #ff6b35;
}

/* Quiz Section */
.quiz-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #2c5aa0 0%, #667eea 100%);
    color: white;
}

.quiz-container {
    max-width: 800px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 40px;
    border-radius: 20px;
}

.quiz-progress {
    margin-bottom: 30px;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 10px;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(45deg, #ff6b35, #f7931e);
    width: 20%;
    transition: width 0.3s ease;
}

.progress-text {
    font-size: 14px;
    opacity: 0.8;
}

.quiz-question {
    margin-bottom: 30px;
}

.quiz-question h3 {
    font-size: 1.5rem;
    margin-bottom: 20px;
}

.quiz-options {
    display: grid;
    gap: 15px;
}

.quiz-option {
    background: rgba(255, 255, 255, 0.1);
    border: 2px solid transparent;
    padding: 15px 20px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.quiz-option:hover {
    background: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 107, 53, 0.5);
}

.quiz-option.selected {
    background: rgba(255, 107, 53, 0.3);
    border-color: #ff6b35;
}

.quiz-navigation {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
}

.results-cards {
    display: grid;
    gap: 20px;
    margin: 30px 0;
}

.result-card {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    backdrop-filter: blur(10px);
}

/* Resources Section */
.resources-section {
    padding: 100px 0;
    background: #f8f9fa;
}

.resources-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 50px;
}

.resource-card {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.resource-card:hover {
    transform: translateY(-5px);
}

.resource-card i {
    font-size: 3rem;
    color: #ff6b35;
    margin-bottom: 20px;
}

.resource-card h3 {
    font-size: 1.5rem;
    margin-bottom: 20px;
    color: #2c5aa0;
}

.resource-card ul {
    list-style: none;
}

.resource-card li {
    padding: 8px 0;
    border-bottom: 1px solid #eee;
    color: #666;
}

.resource-card li:last-child {
    border-bottom: none;
}

/* Stories Section */
.stories-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.stories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 50px;
}

.story-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 15px;
    transition: transform 0.3s ease;
}

.story-card:hover {
    transform: translateY(-5px);
}

.story-image {
    text-align: center;
    margin-bottom: 20px;
}

.avatar {
    font-size: 4rem;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.story-role {
    color: #ff6b35;
    font-weight: 600;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    background: #1a1a1a;
    color: white;
    padding: 50px 0 20px;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 40px;
    margin-bottom: 30px;
}

.footer-section h3,
.footer-section h4 {
    margin-bottom: 20px;
    color: #ff6b35;
}

.footer-section ul {
    list-style: none;
}

.footer-section ul li {
    margin-bottom: 10px;
}

.footer-section ul li a {
    color: #ccc;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-section ul li a:hover {
    color: #ff6b35;
}

.social-links {
    display: flex;
    gap: 15px;
}

.social-links a {
    width: 40px;
    height: 40px;
    background: #ff6b35;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    text-decoration: none;
    transition: transform 0.3s ease;
}

.social-links a:hover {
    transform: translateY(-3px);
}

.footer-bottom {
    text-align: center;
    padding-top: 20px;
    border-top: 1px solid #333;
    color: #ccc;
}

/* Animations */
@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Responsive Design */
@media (max-width: 768px) {
    .hamburger {
        display: flex;
    }
    
    .nav-menu {
        position: fixed;
        left: -100%;
        top: 70px;
        flex-direction: column;
        background-color: white;
        width: 100%;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0 10px 27px rgba(0, 0, 0, 0.05);
        padding: 20px 0;
    }
    
    .nav-menu.active {
        left: 0;
    }
    
    .hero-container {
        grid-template-columns: 1fr;
        text-align: center;
    }
    
    .hero-visual {
        display: none;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .btn {
        width: 100%;
        max-width: 250px;
    }
    
    .careers-grid {
        grid-template-columns: 1fr;
    }
    
    .section-title {
        font-size: 2rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px;
    }
    
    .hero-title {
        font-size: 2rem;
    }
    
    .hero-subtitle {
        font-size: 1rem;
    }
    
    .section-title {
        font-size: 1.8rem;
    }
    
    .modal-content {
        margin: 10% auto;
        padding: 20px;
    }
    
    .quiz-container {
        padding: 20px;
    }
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Loading animation */
.loading {
    opacity: 0;
    animation: fadeIn 0.5s ease-in forwards;
}

@keyframes fadeIn {
    to {
        opacity: 1;
    }
}'''

# Save CSS file
with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("CSS file created successfully!")