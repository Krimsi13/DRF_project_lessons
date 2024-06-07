from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/preview/", **NULLABLE, verbose_name="Картинка"
    )
    description = models.TextField(verbose_name="Описание курса")
    # lessons = models.ManyToManyField(Lesson, verbose_name="Уроки")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(
        upload_to="materials/preview/", **NULLABLE, verbose_name="Картинка"
    )
    link_to_video = models.TextField(verbose_name="Ссылка на видео")

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
