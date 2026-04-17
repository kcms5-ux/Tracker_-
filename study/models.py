from django.db import models


class Study(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('django', 'Django'),
        ('algorithm', '알고리즘'),
        ('database', 'Database'),
        ('etc', '기타'),
    ]

    title = models.CharField(max_length=200, verbose_name='공부 제목')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='django', verbose_name='카테고리')
    study_date = models.DateField(verbose_name='공부 날짜')
    hours = models.PositiveIntegerField(default=0, verbose_name='시간')
    minutes = models.PositiveIntegerField(default=0, verbose_name='분')
    memo = models.TextField(blank=True, verbose_name='메모')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-study_date', '-created_at']
        verbose_name = '공부 기록'
        verbose_name_plural = '공부 기록들'

    def __str__(self):
        return f'{self.title} ({self.study_date})'

    @property
    def total_minutes(self):
        return self.hours * 60 + self.minutes