from django.db import models


class TestMe(models.Model):
    test_m2m = models.ManyToManyField('self', blank=True)
    test_ip = models.IPAddressField()
    test_url = models.URLField()
    test_int = models.IntegerField()
    test_img = models.ImageField(upload_to='dummy', blank=True)
    test_file = models.FileField(upload_to='dummy', blank=True)
    test_date = models.DateField()
    test_char = models.CharField(max_length=50)
    test_bool = models.BooleanField()
    test_time = models.TimeField()
    test_slug = models.SlugField()
    test_text = models.TextField()
    test_email = models.EmailField()
    test_float = models.FloatField()
    test_bigint = models.BigIntegerField()
    test_positive_integer = models.PositiveIntegerField()
    test_decimal = models.DecimalField(max_digits=5, decimal_places=2)
    test_comma_separated_int = models.CommaSeparatedIntegerField(max_length=100)
    test_small_int = models.SmallIntegerField()
    test_nullbool = models.NullBooleanField()
    test_filepath = models.FilePathField(blank=True)
    test_positive_small_int = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = u'Test me'
        verbose_name_plural = u'Lot of Test me'


class TestMeProxyForFieldsets(TestMe):
    class Meta:
        proxy = True
        verbose_name = u'Test me fieldsets'
        verbose_name_plural = u'Lot of Test me fieldsets'


class TestThat(models.Model):
    that = models.ForeignKey(TestMe)
    test_ip = models.IPAddressField()
    test_url = models.URLField()
    test_int = models.IntegerField()
    test_date = models.DateField()
    test_bool = models.BooleanField()

    class Meta:
        verbose_name = u'Test that'
        verbose_name_plural = u'Lot of Test that'


class TestSortable(models.Model):
    that = models.ForeignKey(TestMe)
    position = models.PositiveSmallIntegerField("Position")
    test_char = models.CharField(max_length=5)

    class Meta:
        ordering = ('position', )
