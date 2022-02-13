from django.db import models


class AbstractManager(models.Manager):
    def get_queryset(self):
        return super(AbstractManager, self).get_queryset().filter(is_deleted=False)

    def get_all(self):
        return super(AbstractManager, self).get_queryset()


class AbstractModel(models.Model):
    is_deleted = models.BooleanField(
        verbose_name='Is deleted',
        default=False,
    )

    is_active = models.BooleanField(
        verbose_name='Is active',
        default=True,
    )
    create_date = models.DateField(
        verbose_name='Create Date',
        auto_now=True,
    )

    objects = AbstractManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
