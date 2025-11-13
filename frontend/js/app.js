// API Configuration
// Automatically detect API URL based on current host
// For production, set this to your backend API URL
const getApiBaseUrl = () => {
    // Check if API_BASE_URL is set in window (can be set in HTML)
    if (window.API_BASE_URL) {
        return window.API_BASE_URL;
    }
    
    // Auto-detect based on current host
    const hostname = window.location.hostname;
    const protocol = window.location.protocol;
    const port = window.location.port;
    
    // If running on same domain (production), use same origin
    if (hostname !== 'localhost' && hostname !== '127.0.0.1') {
        return `${protocol}//${hostname}${port ? ':' + port : ''}/api`;
    }
    
    // Development fallback
    return 'http://localhost:8000/api';
};

const API_BASE_URL = getApiBaseUrl();

// API Functions
const api = {
    async fetchAbout() {
        try {
            console.log('Fetching from:', `${API_BASE_URL}/about/`);
            const response = await fetch(`${API_BASE_URL}/about/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                mode: 'cors'
            });
            console.log('Response status:', response.status, response.statusText);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            console.log('About data received:', data);
            
            // Handle paginated response
            const results = Array.isArray(data) ? data : (data.results || []);
            return results.length > 0 ? results[0] : null;
        } catch (error) {
            console.error('Error fetching about:', error);
            console.error('Error details:', error.message, error.stack);
            return null;
        }
    },

    async fetchExperiences() {
        try {
            const response = await fetch(`${API_BASE_URL}/experiences/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                mode: 'cors'
            });
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching experiences:', error);
            return [];
        }
    },

    async fetchProjects() {
        try {
            const response = await fetch(`${API_BASE_URL}/projects/`);
            if (!response.ok) throw new Error('Failed to fetch projects');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching projects:', error);
            return [];
        }
    },

    async fetchSkills() {
        try {
            const response = await fetch(`${API_BASE_URL}/skills/`);
            if (!response.ok) throw new Error('Failed to fetch skills');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching skills:', error);
            return [];
        }
    },

    async fetchEducation() {
        try {
            const response = await fetch(`${API_BASE_URL}/education/`);
            if (!response.ok) throw new Error('Failed to fetch education');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching education:', error);
            return [];
        }
    },

    async fetchContact() {
        try {
            const response = await fetch(`${API_BASE_URL}/contact/`);
            if (!response.ok) throw new Error('Failed to fetch contact info');
            const data = await response.json();
            // Handle paginated response
            const results = Array.isArray(data) ? data : (data.results || []);
            return results.length > 0 ? results[0] : null;
        } catch (error) {
            console.error('Error fetching contact:', error);
            return null;
        }
    },

    async fetchSocialLinks() {
        try {
            const response = await fetch(`${API_BASE_URL}/social-links/`);
            if (!response.ok) throw new Error('Failed to fetch social links');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching social links:', error);
            return [];
        }
    },

    async fetchAwards() {
        try {
            const response = await fetch(`${API_BASE_URL}/awards/`);
            if (!response.ok) throw new Error('Failed to fetch awards');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching awards:', error);
            return [];
        }
    },

    async fetchHobbies() {
        try {
            const response = await fetch(`${API_BASE_URL}/hobbies/`);
            if (!response.ok) throw new Error('Failed to fetch hobbies');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching hobbies:', error);
            return [];
        }
    },

    async fetchStatistics() {
        try {
            const response = await fetch(`${API_BASE_URL}/statistics/`);
            if (!response.ok) throw new Error('Failed to fetch statistics');
            const data = await response.json();
            // Handle paginated response
            const results = Array.isArray(data) ? data : (data.results || []);
            return results.length > 0 ? results[0] : null;
        } catch (error) {
            console.error('Error fetching statistics:', error);
            return null;
        }
    },

    async fetchTestimonials() {
        try {
            const response = await fetch(`${API_BASE_URL}/testimonials/`);
            if (!response.ok) throw new Error('Failed to fetch testimonials');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching testimonials:', error);
            return [];
        }
    },

    async fetchSkillAttributes() {
        try {
            const response = await fetch(`${API_BASE_URL}/skill-attributes/`);
            if (!response.ok) throw new Error('Failed to fetch skill attributes');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching skill attributes:', error);
            return [];
        }
    },

    async fetchNavigationItems() {
        try {
            const response = await fetch(`${API_BASE_URL}/navigation-items/`);
            if (!response.ok) throw new Error('Failed to fetch navigation items');
            const data = await response.json();
            // Handle paginated response
            return Array.isArray(data) ? data : (data.results || []);
        } catch (error) {
            console.error('Error fetching navigation items:', error);
            return [];
        }
    },

    async fetchSiteSettings() {
        try {
            const response = await fetch(`${API_BASE_URL}/site-settings/public/`);
            if (!response.ok) throw new Error('Failed to fetch site settings');
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching site settings:', error);
            return null;
        }
    }
};

// Render Functions
const render = {
    about(data) {
        const nameEl = document.getElementById('hero-name');
        const titleEl = document.getElementById('hero-title');
        const bioEl = document.getElementById('hero-bio');
        const navLogoEl = document.getElementById('nav-logo');
        const aboutWrapperEl = document.getElementById('about-wrapper');
        const profileImgEl = document.getElementById('profile-image');
        const footerNameEl = document.getElementById('footer-name');
        const aboutSection = document.getElementById('about');

        if (!data) {
            // No about data - show default message
            if (aboutSection) aboutSection.classList.add('hidden-section');
            if (nameEl) nameEl.textContent = 'Your Name';
            if (titleEl) titleEl.textContent = 'Developer • Traveler • Freelancer';
            if (bioEl) bioEl.textContent = 'Welcome to my portfolio';
            if (navLogoEl) navLogoEl.textContent = 'Portfolio';
            if (footerNameEl) footerNameEl.textContent = 'Portfolio';
            if (profileImgEl) {
                profileImgEl.style.display = 'block';
                profileImgEl.src = '';
            }
            // Show default button when no data
            const heroActionsEl = document.getElementById('hero-actions');
            if (heroActionsEl) {
                heroActionsEl.innerHTML = '<a href="#about" class="btn btn-secondary">Learn More</a>';
            }
            if (aboutWrapperEl) aboutWrapperEl.innerHTML = '<p>No content available. Please add your information in the admin panel.</p>';
            return;
        }

        // Update hero name
        if (nameEl) nameEl.textContent = data.name || 'Your Name';
        if (navLogoEl) navLogoEl.textContent = data.name || 'Portfolio';
        if (footerNameEl) footerNameEl.textContent = data.name || 'Portfolio';

        // Update hero title (tagline from backend)
        if (titleEl) {
            titleEl.textContent = data.tagline || 'Developer • Traveler • Freelancer';
        }

        // Update hero bio
        if (bioEl) {
            bioEl.textContent = data.bio || 'Welcome to my portfolio';
        }

        // Render hero button (configurable from backend)
        const heroActionsEl = document.getElementById('hero-actions');
        if (heroActionsEl) {
            if (data.show_hero_button !== false) {
                const buttonText = data.hero_button_text || 'Learn More';
                const buttonLink = data.hero_button_link || '#about';
                heroActionsEl.innerHTML = `<a href="${buttonLink}" class="btn btn-secondary">${buttonText}</a>`;
            } else {
                heroActionsEl.innerHTML = '';
            }
        }

        // Update profile image in hero with shape
        if (data.profile_image_url && profileImgEl) {
            profileImgEl.src = data.profile_image_url;
            profileImgEl.alt = data.name;
            profileImgEl.style.display = 'block';
            // Apply image shape class
            const imageShape = data.image_shape || 'rounded';
            profileImgEl.className = `hero-profile-img img-shape-${imageShape}`;
        } else if (profileImgEl) {
            profileImgEl.style.display = 'block';
            const imageShape = data.image_shape || 'rounded';
            profileImgEl.className = `hero-profile-img img-shape-${imageShape}`;
        }

        // Render new About section layout
        if (aboutWrapperEl) {
            const showImage = data.show_about_image !== false; // Default to true if not set
            const imageShape = data.image_shape || 'rounded';
            const profileImageHtml = showImage && data.profile_image_url 
                ? `<div class="about-profile-image"><img src="${data.profile_image_url}" alt="${data.name}" class="about-img img-shape-${imageShape}"></div>`
                : showImage && !data.profile_image_url
                ? `<div class="about-profile-image"><div class="about-img-placeholder img-shape-${imageShape}"></div></div>`
                : '';
            
            const personalDetailsHtml = `
                <div class="personal-details">
                    <div class="detail-item">
                        <strong>Name:</strong> <span>${data.name || 'N/A'}</span>
                    </div>
                    ${data.age ? `<div class="detail-item"><strong>Age:</strong> <span>${data.age} Years</span></div>` : ''}
                    ${data.website ? `<div class="detail-item"><strong>Website:</strong> <a href="${data.website}" target="_blank">${data.website}</a></div>` : ''}
                    ${data.home_country ? `<div class="detail-item"><strong>Home Country:</strong> <span>${data.home_country}</span></div>` : ''}
                </div>
            `;

            const actionButtonsHtml = `
                <div class="about-actions">
                    <a href="#contact" class="btn-hire-me">Hire Me For Work.</a>
                    ${data.resume_url ? `<a href="${data.resume_url}" download class="btn-download-resume"><span class="download-icon">↓</span> Download Resume</a>` : ''}
                </div>
            `;

            // Adjust layout class if image is hidden
            const layoutClass = showImage ? 'about-layout' : 'about-layout about-layout-no-image';
            aboutWrapperEl.innerHTML = `
                <div class="${layoutClass}">
                    ${profileImageHtml}
                    <div class="about-content-right">
                        <div class="about-text">
                            <p>${data.bio || 'No bio available.'}</p>
                        </div>
                        ${personalDetailsHtml}
                        ${actionButtonsHtml}
                    </div>
                </div>
            `;
        }
    },

    diamondLabels(hobbies, skills) {
        // Update diamond labels with hobbies or skill categories
        const labels = document.querySelectorAll('.diamond-label');
        const labelTexts = [];
        
        // Get first 3 hobbies, or use skill categories, or default labels
        if (hobbies && hobbies.length > 0) {
            labelTexts.push(hobbies[0].name.toLowerCase());
            if (hobbies.length > 1) labelTexts.push(hobbies[1].name.toLowerCase());
            if (hobbies.length > 2) labelTexts.push(hobbies[2].name.toLowerCase());
        } else if (skills && skills.length > 0) {
            // Get unique skill categories
            const categories = [...new Set(skills.map(s => s.category).filter(c => c))];
            labelTexts.push(...categories.slice(0, 3).map(c => c.toLowerCase()));
        }
        
        // Default labels if nothing available
        if (labelTexts.length === 0) {
            labelTexts.push('developer', 'traveler', 'freelancer');
        }
        
        // Pad with defaults if needed
        while (labelTexts.length < 3) {
            const defaults = ['developer', 'traveler', 'freelancer'];
            labelTexts.push(defaults[labelTexts.length]);
        }
        
        // Update label texts
        labels.forEach((label, index) => {
            if (labelTexts[index]) {
                label.textContent = labelTexts[index];
            }
        });
    },

    socialLinks(links) {
        // Ensure links is an array
        if (!links || !Array.isArray(links) || links.length === 0) {
            return;
        }

        const footerSocialEl = document.getElementById('footer-social');

        const createLink = (link) => {
            const a = document.createElement('a');
            a.href = link.url;
            a.target = '_blank';
            a.rel = 'noopener noreferrer';
            a.className = 'social-link';
            a.innerHTML = link.icon || link.platform.charAt(0).toUpperCase();
            a.title = link.platform;
            return a;
        };

        if (footerSocialEl) {
            footerSocialEl.innerHTML = '';
            links.forEach(link => {
                footerSocialEl.appendChild(createLink(link));
            });
        }
    },

    skills(skills) {
        if (!skills || skills.length === 0) {
            document.getElementById('skills').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('skills-container');
        if (!container) return;

        // Group skills by category
        const skillsByCategory = {};
        skills.forEach(skill => {
            const category = skill.category || 'Other';
            if (!skillsByCategory[category]) {
                skillsByCategory[category] = [];
            }
            skillsByCategory[category].push(skill);
        });

        container.innerHTML = Object.keys(skillsByCategory).map(category => {
            const categorySkills = skillsByCategory[category];
            const skillsHtml = categorySkills.map(skill => `
                <div class="skill-item">
                    <div class="skill-name">
                        <span>${skill.name}</span>
                    </div>
                </div>
            `).join('');

            return `
                <div class="skill-card">
                    <div class="skill-category">${category}</div>
                    ${skillsHtml}
                </div>
            `;
        }).join('');
    },

    experiences(experiences) {
        if (!experiences || experiences.length === 0) {
            document.getElementById('experience').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('experience-container');
        if (!container) return;

        container.innerHTML = experiences.map(exp => {
            const endDate = exp.end_date || 'Present';
            return `
                <div class="timeline-item">
                    <div class="timeline-title">${exp.title}</div>
                    <div class="timeline-company">${exp.company}</div>
                    <div class="timeline-date">${exp.start_date} - ${endDate}</div>
                    <div class="timeline-description">${exp.description}</div>
                </div>
            `;
        }).join('');
    },

    projects(projects) {
        if (!projects || projects.length === 0) {
            document.getElementById('projects').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('projects-container');
        if (!container) return;

        container.innerHTML = projects.map(project => {
            const imageShape = project.image_shape || 'rounded';
            const imageHtml = project.image_url 
                ? `<img src="${project.image_url}" alt="${project.title}" class="project-image img-shape-${imageShape}">`
                : '';
            const linkHtml = project.link 
                ? `<a href="${project.link}" target="_blank" rel="noopener noreferrer" class="project-link">View Project →</a>`
                : '';
            const technologies = project.technologies 
                ? project.technologies.split(',').map(tech => tech.trim())
                : [];
            const techHtml = technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('');

            return `
                <div class="project-card">
                    ${imageHtml}
                    <div class="project-content">
                        <h3 class="project-title">${project.title}</h3>
                        <p class="project-description">${project.description}</p>
                        ${techHtml ? `<div class="project-technologies">${techHtml}</div>` : ''}
                        ${linkHtml}
                    </div>
                </div>
            `;
        }).join('');
    },

    education(education) {
        if (!education || education.length === 0) {
            document.getElementById('education').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('education-container');
        if (!container) return;

        container.innerHTML = education.map(edu => {
            const endDate = edu.end_date || 'Present';
            const description = edu.description ? `<div class="timeline-description">${edu.description}</div>` : '';
            return `
                <div class="timeline-item">
                    <div class="timeline-title">${edu.degree}</div>
                    <div class="timeline-company">${edu.institution}</div>
                    <div class="timeline-date">${edu.start_date} - ${endDate}</div>
                    ${description}
                </div>
            `;
        }).join('');
    },

    awards(awards) {
        if (!awards || awards.length === 0) {
            document.getElementById('awards').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('awards-container');
        if (!container) return;

        container.innerHTML = awards.map(award => {
            const description = award.description ? `<p class="award-description">${award.description}</p>` : '';
            const issuer = award.issuer ? `<div class="award-issuer">${award.issuer}</div>` : '';
            return `
                <div class="award-card">
                    <h3 class="award-title">${award.title}</h3>
                    ${issuer}
                    <div class="award-date">${award.date}</div>
                    ${description}
                </div>
            `;
        }).join('');
    },

    hobbies(hobbies) {
        if (!hobbies || hobbies.length === 0) {
            document.getElementById('hobbies').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('hobbies-container');
        if (!container) return;

        container.innerHTML = hobbies.map(hobby => {
            const description = hobby.description ? `<p class="hobby-description">${hobby.description}</p>` : '';
            const icon = hobby.icon || '🎯';
            return `
                <div class="hobby-card">
                    <div class="hobby-icon">${icon}</div>
                    <h3 class="hobby-name">${hobby.name}</h3>
                    ${description}
                </div>
            `;
        }).join('');
    },

    contact(contact) {
        if (!contact) {
            document.getElementById('contact').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('contact-content');
        if (!container) return;

        const emailHtml = contact.email 
            ? `<div class="contact-item">
                <strong>Email:</strong>
                <a href="mailto:${contact.email}">${contact.email}</a>
               </div>`
            : '';
        const phoneHtml = contact.phone 
            ? `<div class="contact-item">
                <strong>Phone:</strong>
                <a href="tel:${contact.phone}">${contact.phone}</a>
               </div>`
            : '';
        const locationHtml = contact.location 
            ? `<div class="contact-item">
                <strong>Location:</strong>
                <span>${contact.location}</span>
               </div>`
            : '';

        container.innerHTML = `
            <div class="contact-info">
                ${emailHtml}
                ${phoneHtml}
                ${locationHtml}
            </div>
        `;
    },

    skillAttributes(attributes) {
        if (!attributes || attributes.length === 0) {
            document.getElementById('skill-attributes').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('skill-attributes-container');
        if (!container) return;

        container.innerHTML = attributes.map(attr => {
            const icon = attr.icon || '⭐';
            return `
                <div class="skill-attribute-item">
                    <div class="skill-attribute-icon">
                        <span class="icon-content">${icon}</span>
                    </div>
                    <div class="skill-attribute-name">${attr.name}</div>
                </div>
            `;
        }).join('');
    },

    statistics(stats) {
        if (!stats) {
            document.getElementById('statistics').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('statistics-container');
        if (!container) return;

        container.innerHTML = `
            <div class="stat-item">
                <div class="stat-number">${stats.awards_won || 0}</div>
                <div class="stat-label">Awards Won</div>
            </div>
            <div class="stat-separator">◆</div>
            <div class="stat-item">
                <div class="stat-number">${stats.happy_customers || 0}+</div>
                <div class="stat-label">Happy Customers</div>
            </div>
            <div class="stat-separator">◆</div>
            <div class="stat-item">
                <div class="stat-number">${stats.projects_done || 0}+</div>
                <div class="stat-label">Projects Done</div>
            </div>
            <div class="stat-separator">◆</div>
            <div class="stat-item">
                <div class="stat-number">${stats.games_played || '0hrs'}</div>
                <div class="stat-label">Games Played</div>
            </div>
        `;
    },

    testimonials(testimonials) {
        if (!testimonials || testimonials.length === 0) {
            document.getElementById('testimonials').classList.add('hidden-section');
            return;
        }

        const container = document.getElementById('testimonials-container');
        if (!container) return;

        // Show first testimonial (or all if you want to show multiple)
        const testimonial = testimonials[0];
        const authorTitle = testimonial.author_title ? `${testimonial.author_title}` : '';
        const authorCompany = testimonial.author_company ? ` at ${testimonial.author_company}` : '';
        const authorInfo = authorTitle || authorCompany ? `${authorTitle}${authorCompany}` : '';

        container.innerHTML = `
            <div class="testimonial-item">
                <blockquote class="testimonial-quote">${testimonial.quote}</blockquote>
                <div class="testimonial-author">
                    <div class="author-name">${testimonial.author_name}</div>
                    ${authorInfo ? `<div class="author-title">${authorInfo}</div>` : ''}
                </div>
            </div>
        `;
    },

    navigation(navItems) {
        const navMenuEl = document.getElementById('nav-menu');
        if (!navMenuEl) return;

        if (!navItems || navItems.length === 0) {
            // Use default navigation if none configured
            return;
        }

        // Clear existing navigation
        navMenuEl.innerHTML = '';

        // Render navigation items
        navItems.forEach(item => {
            const link = document.createElement('a');
            link.href = item.link;
            link.textContent = item.label;
            link.className = 'nav-link';
            if (item.is_cta) {
                link.classList.add('nav-link-cta');
            }
            navMenuEl.appendChild(link);
        });
    },

    siteSettings(settings) {
        if (!settings) return;

        // Update section titles
        const sectionTitleMap = {
            'about': settings.about_title,
            'skills': settings.skills_title,
            'experience': settings.experience_title,
            'projects': settings.projects_title,
            'education': settings.education_title,
            'awards': settings.awards_title,
            'hobbies': settings.hobbies_title,
            'contact': settings.contact_title,
            'testimonials': settings.testimonials_title
        };

        Object.keys(sectionTitleMap).forEach(sectionId => {
            const section = document.getElementById(sectionId);
            if (section) {
                const titleEl = section.querySelector('.section-title');
                if (titleEl && sectionTitleMap[sectionId]) {
                    titleEl.textContent = sectionTitleMap[sectionId];
                }
            }
        });

        // Update footer text
        const footerTextEl = document.querySelector('.footer p');
        if (footerTextEl && settings.footer_text) {
            const year = settings.copyright_year || new Date().getFullYear();
            const footerName = document.getElementById('footer-name')?.textContent || 'Portfolio';
            footerTextEl.innerHTML = `&copy; ${year} ${footerName}. ${settings.footer_text}`;
        }
    }
};

// Initialize App
async function initApp() {
    const loader = document.getElementById('loader');
    
    try {
        console.log('Fetching portfolio data from API...');
        
        // Fetch all data in parallel
        const [about, experiences, projects, skills, education, contact, socialLinks, awards, hobbies, statistics, testimonials, skillAttributes, navigationItems, siteSettings] = await Promise.all([
            api.fetchAbout(),
            api.fetchExperiences(),
            api.fetchProjects(),
            api.fetchSkills(),
            api.fetchEducation(),
            api.fetchContact(),
            api.fetchSocialLinks(),
            api.fetchAwards(),
            api.fetchHobbies(),
            api.fetchStatistics(),
            api.fetchTestimonials(),
            api.fetchSkillAttributes(),
            api.fetchNavigationItems(),
            api.fetchSiteSettings()
        ]);

        console.log('Data fetched:', { about, experiences, projects, skills, education, contact, socialLinks, awards, hobbies, statistics, testimonials, skillAttributes, navigationItems, siteSettings });

        // Render all data
        render.about(about);
        render.navigation(navigationItems);
        render.siteSettings(siteSettings);
        render.socialLinks(socialLinks);
        render.skills(skills);
        render.experiences(experiences);
        render.projects(projects);
        render.education(education);
        render.awards(awards);
        render.hobbies(hobbies);
        render.contact(contact);
        render.skillAttributes(skillAttributes);
        render.statistics(statistics);
        render.testimonials(testimonials);

        // Hide loader
        setTimeout(() => {
            if (loader) {
                loader.classList.add('hidden');
            }
        }, 500);
        
        // Show message if no content
        if (!about && !experiences.length && !projects.length && !skills.length) {
            console.warn('No content found. Please add content via admin panel at http://127.0.0.1:8000/admin');
        }
    } catch (error) {
        console.error('Error initializing app:', error);
        console.error('Make sure the backend server is running on http://127.0.0.1:8000');
        
        // Show error message to user
        const nameEl = document.getElementById('hero-name');
        if (nameEl) nameEl.textContent = 'Error Loading Portfolio';
        
        if (loader) {
            loader.classList.add('hidden');
        }
    }
}

// Set current year and initialize
document.addEventListener('DOMContentLoaded', () => {
    const yearEl = document.getElementById('current-year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }
    initApp();
});

