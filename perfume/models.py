from django.db import models


class Image(models.Model):
    ten = models.CharField(max_length=50)
    image = models.ImageField(verbose_name=ten, max_length=1000)


class Nhom_huong(models.Model):
    ten = models.CharField(max_length=40)
    mo_ta = models.TextField(default='')
    image = models.ManyToManyField(Image, related_name='image_nhom_huong')

    def __str__(self):
        return self.ten


class Mui_huong(models.Model):
    ten = models.CharField(max_length=40)
    nhom_mui = models.ForeignKey(Nhom_huong, on_delete=models.PROTECT, related_name='nhom_huong')
    mo_ta = models.TextField(default='')
    image = models.ManyToManyField(Image, related_name='image_mui_huong')

    def __str__(self):
        return self.ten


class Pha_che(models.Model):
    ten = models.CharField(max_length=40)
    gioi_thieu = models.TextField()
    image = models.ManyToManyField(Image, related_name='image_pha_che')

    def __str__(self):
        return self.ten


class Thuong_hieu(models.Model):
    ten = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    gioi_thieu = models.TextField()
    website = models.URLField()
    image = models.ManyToManyField(Image, related_name='image_thuong_heu')

    def __str__(self):
        return self.ten


class Nuoc_hoa(models.Model):
    ten = models.CharField(max_length=40)
    thuong_hieu = models.ForeignKey(Thuong_hieu, related_name='thuong_hieu', on_delete=models.PROTECT, blank=True, null=True)
    nhom_nuoc_hoa = models.CharField(max_length=60, blank=True, null=True)
    gioi_tinh = models.CharField(max_length=8, blank=True, null=True)
    do_tuoi = models.CharField(max_length=70, blank=True, null=True)
    nam_sx = models.CharField(max_length=70, blank=True, null=True)
    nong_do = models.CharField(max_length=30, blank=True, null=True)
    pha_che = models.ForeignKey(Pha_che, related_name='pha_che', on_delete=models.PROTECT, blank=True, null=True)
    do_luu = models.CharField(max_length=30, blank=True, null=True)
    do_toa = models.CharField(max_length=30, blank=True, null=True)
    khuyen_dung = models.CharField(max_length=60, blank=True, null=True)
    phong_cach = models.CharField(max_length=80, blank=True, null=True)
    huong_dau = models.ManyToManyField(Mui_huong, related_name='huong_dau', blank=True, null=True)
    huong_chinh = models.ManyToManyField(Mui_huong, related_name='huong_chinh', blank=True, null=True)
    huong_cuoi = models.ManyToManyField(Mui_huong, related_name='huong_cuoi', blank=True, null=True)
    diem = models.DecimalField(max_digits=4, decimal_places=2)
    tong_quan = models.TextField()
    chi_tiet = models.TextField()
    image = models.ManyToManyField(Image, related_name='image_nuuoc_hoa')

    def __str__(self):
        return self.ten


class Gia(models.Model):
    nuoc_hoa = models.ForeignKey(Nuoc_hoa, related_name='nuoc_hoa', on_delete=models.CASCADE)
    gia = models.IntegerField()
    dia_diem = models.CharField(max_length=50)

    def __str__(self):
        return self.nuoc_hoa.__str__()


class Blog(models.Model):
    title = models.CharField(max_length=50)
    date_create = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title
