from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from .models import (
    About, Experience, Project, Skill, Education,
    ContactInfo, SocialLink, Award, Hobby,
    Statistics, Testimonial, SkillAttribute,
    NavigationItem, SiteSettings
)
from .serializers import (
    AboutSerializer, ExperienceSerializer, ProjectSerializer,
    SkillSerializer, EducationSerializer, ContactInfoSerializer,
    SocialLinkSerializer, AwardSerializer, HobbySerializer,
    StatisticsSerializer, TestimonialSerializer, SkillAttributeSerializer,
    NavigationItemSerializer, SiteSettingsSerializer
)


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        queryset = About.objects.all()
        # Filter by enabled for public access
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        """Public endpoint that only returns enabled items"""
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def download_resume(self, request, pk=None):
        """Download resume file"""
        about = self.get_object()
        if about.resume:
            return FileResponse(about.resume.open(), as_attachment=True, filename=about.resume.name)
        return Response({'error': 'Resume not found'}, status=404)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        queryset = Experience.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        queryset = Project.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_queryset(self):
        queryset = Education.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    def get_queryset(self):
        queryset = ContactInfo.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

    def get_queryset(self):
        queryset = SocialLink.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

    def get_queryset(self):
        queryset = Award.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

    def get_queryset(self):
        queryset = Hobby.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        queryset = Statistics.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        queryset = Testimonial.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SkillAttributeViewSet(viewsets.ModelViewSet):
    queryset = SkillAttribute.objects.all()
    serializer_class = SkillAttributeSerializer

    def get_queryset(self):
        queryset = SkillAttribute.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NavigationItemViewSet(viewsets.ModelViewSet):
    queryset = NavigationItem.objects.all()
    serializer_class = NavigationItemSerializer

    def get_queryset(self):
        queryset = NavigationItem.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(enabled=True)
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        queryset = self.get_queryset().filter(enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SiteSettingsViewSet(viewsets.ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

    def get_queryset(self):
        # SiteSettings should only have one instance
        queryset = SiteSettings.objects.all()
        if not queryset.exists():
            # Create default instance if none exists
            SiteSettings.objects.create()
            queryset = SiteSettings.objects.all()
        return queryset

    @action(detail=False, methods=['get'])
    def public(self, request):
        """Public endpoint that returns the first (and only) SiteSettings instance"""
        settings = SiteSettings.objects.first()
        if not settings:
            settings = SiteSettings.objects.create()
        serializer = self.get_serializer(settings)
        return Response(serializer.data)

