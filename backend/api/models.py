from django.db import models
from django.utils import timezone


class About(models.Model):
    """About section with name, bio, profile image, and personal details"""
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    image_shape = models.CharField(
        max_length=20,
        choices=[
            ('rounded', 'Rounded'),
            ('square', 'Square'),
            ('circle', 'Circle'),
            ('diamond', 'Diamond'),
        ],
        default='rounded',
        help_text="Shape style for profile image"
    )
    show_about_image = models.BooleanField(default=True, help_text="Show/hide profile image in About section")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="Upload PDF or DOCX resume")
    age = models.IntegerField(blank=True, null=True, help_text="Age in years")
    website = models.URLField(blank=True, null=True)
    home_country = models.CharField(max_length=200, blank=True, null=True)
    # Hero section configuration
    tagline = models.CharField(max_length=200, blank=True, null=True, help_text="Hero section tagline (e.g., 'Developer • Traveler • Freelancer')")
    hero_button_text = models.CharField(max_length=100, blank=True, null=True, default="Learn More", help_text="Text for the hero action button")
    hero_button_link = models.CharField(max_length=200, blank=True, null=True, default="#about", help_text="Link URL for the hero action button (e.g., '#about', '/contact', 'https://...')")
    show_hero_button = models.BooleanField(default=True, help_text="Show/hide the hero action button")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        ordering = ['-updated_at']

    def __str__(self):
        return self.name


class Experience(models.Model):
    """Work experience"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Project(models.Model):
    """Project portfolio"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_shape = models.CharField(
        max_length=20,
        choices=[
            ('rounded', 'Rounded'),
            ('square', 'Square'),
            ('circle', 'Circle'),
            ('diamond', 'Diamond'),
        ],
        default='rounded',
        help_text="Shape style for project image"
    )
    link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Skills with categories"""
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Education(models.Model):
    """Education history"""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class ContactInfo(models.Model):
    """Contact information"""
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        ordering = ['-updated_at']

    def __str__(self):
        return self.email


class SocialLink(models.Model):
    """Social media links"""
    platform = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Icon class name or emoji")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering = ['platform']

    def __str__(self):
        return self.platform


class Award(models.Model):
    """Awards and achievements"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    issuer = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Awards"
        ordering = ['-date']

    def __str__(self):
        return self.title


class Hobby(models.Model):
    """Hobbies and interests"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Icon class name or emoji")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Statistics(models.Model):
    """Statistics for portfolio (awards, customers, projects, games)"""
    awards_won = models.IntegerField(default=0)
    happy_customers = models.IntegerField(default=0)
    projects_done = models.IntegerField(default=0)
    games_played = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., '4000hrs' or '4000 hrs'")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"
        ordering = ['-updated_at']

    def __str__(self):
        return f"Stats: {self.awards_won} awards, {self.happy_customers} customers"


class Testimonial(models.Model):
    """Testimonials from clients/colleagues"""
    quote = models.TextField()
    author_name = models.CharField(max_length=200)
    author_title = models.CharField(max_length=200, blank=True, null=True)
    author_company = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial from {self.author_name}"


class SkillAttribute(models.Model):
    """Skill attributes with icons (Creative, Winner, Smart, etc.)"""
    name = models.CharField(max_length=100, help_text="e.g., Creative, Winner, Smart, Powerful")
    icon = models.CharField(max_length=50, help_text="Icon class name, emoji, or icon identifier")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skill Attribute"
        verbose_name_plural = "Skill Attributes"
        ordering = ['name']

    def __str__(self):
        return self.name


class NavigationItem(models.Model):
    """Navigation menu items"""
    label = models.CharField(max_length=100, help_text="Menu item label (e.g., 'Home', 'About', 'Contact')")
    link = models.CharField(max_length=200, help_text="Link URL (e.g., '#home', '#about', '/contact')")
    is_cta = models.BooleanField(default=False, help_text="Mark as Call-to-Action button (styled differently)")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"
        ordering = ['order', 'label']

    def __str__(self):
        return f"{self.label} ({self.link})"


class SiteSettings(models.Model):
    """Site-wide settings and section titles"""
    # Section Titles
    about_title = models.CharField(max_length=200, default="Basic Info About Me", blank=True, null=True)
    skills_title = models.CharField(max_length=200, default="Skills", blank=True, null=True)
    experience_title = models.CharField(max_length=200, default="Experience", blank=True, null=True)
    projects_title = models.CharField(max_length=200, default="Projects", blank=True, null=True)
    education_title = models.CharField(max_length=200, default="Education", blank=True, null=True)
    awards_title = models.CharField(max_length=200, default="Awards", blank=True, null=True)
    hobbies_title = models.CharField(max_length=200, default="Hobbies", blank=True, null=True)
    contact_title = models.CharField(max_length=200, default="Contact", blank=True, null=True)
    testimonials_title = models.CharField(max_length=200, default="Testimonials", blank=True, null=True)
    
    # Footer
    footer_text = models.CharField(max_length=500, default="All rights reserved.", blank=True, null=True)
    copyright_year = models.IntegerField(blank=True, null=True, help_text="Leave empty to use current year")
    
    # Meta
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
        ordering = ['-updated_at']

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one SiteSettings instance exists
        self.pk = 1
        super().save(*args, **kwargs)

