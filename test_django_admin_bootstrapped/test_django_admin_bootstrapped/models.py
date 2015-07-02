from django.db import models


class TestMe(models.Model):
    test_m2m = models.ManyToManyField('self', blank=True, help_text="Lorem dolor")
    test_ip = models.GenericIPAddressField(help_text="Lorem dolor")
    test_url = models.URLField(help_text="Lorem dolor")
    test_int = models.IntegerField(help_text="Lorem dolor")
    test_img = models.ImageField(upload_to='dummy', blank=True)
    test_file = models.FileField(upload_to='dummy', blank=True)
    test_date = models.DateField(help_text="Lorem dolor")
    test_char = models.CharField(max_length=50, help_text="Lorem dolor")
    test_bool = models.BooleanField(help_text="Lorem dolor", default=False)
    test_time = models.TimeField(help_text="Lorem dolor")
    test_slug = models.SlugField(help_text="Lorem dolor")
    test_text = models.TextField(help_text="Lorem dolor")
    test_email = models.EmailField(help_text="Lorem dolor")
    test_float = models.FloatField(help_text="Lorem dolor")
    test_bigint = models.BigIntegerField(help_text="Lorem dolor")
    test_positive_integer = models.PositiveIntegerField(help_text="Lorem dolor")
    test_decimal = models.DecimalField(max_digits=5, decimal_places=2, help_text="Lorem dolor")
    test_comma_separated_int = models.CommaSeparatedIntegerField(max_length=100, help_text="Lorem dolor")
    test_small_int = models.SmallIntegerField(help_text="Lorem dolor")
    test_nullbool = models.NullBooleanField(help_text="Lorem dolor")
    test_filepath = models.FilePathField(blank=True, help_text="Lorem dolor")
    test_positive_small_int = models.PositiveSmallIntegerField(help_text="Lorem dolor")

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = u'Test me'
        verbose_name_plural = u'Lot of Test me'


class TestMeProxyForFieldsets(TestMe):
    class Meta:
        proxy = True
        verbose_name = u'Test me fieldsets'
        verbose_name_plural = u'Lot of Test me fieldsets'


class TestThat(models.Model):
    that = models.ForeignKey(TestMe, help_text="Lorem dolor")
    test_ip = models.GenericIPAddressField(help_text="Lorem dolor")
    test_url = models.URLField(help_text="Lorem dolor")
    test_int = models.IntegerField(help_text="Lorem dolor")
    test_date = models.DateField(help_text="Lorem dolor")
    test_bool = models.BooleanField(help_text="Lorem dolor", default=True)
    test_fk = models.ForeignKey('TestSortable', help_text="Lorem dolor", null=True, blank=True)

    class Meta:
        verbose_name = u'Test that'
        verbose_name_plural = u'Lot of Test that'


class TestSortable(models.Model):
    that = models.ForeignKey(TestMe)
    position = models.PositiveSmallIntegerField("Position")
    test_char = models.CharField(max_length=5)

    class Meta:
        ordering = ('position', )
