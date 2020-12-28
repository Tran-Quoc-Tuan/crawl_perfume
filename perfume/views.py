from .models import Image, Nhom_huong, Mui_huong, Pha_che, Thuong_hieu, Nuoc_hoa, Gia, Blog
from .serializers import ImageSerializer, Nhom_huongSerializer, Mui_huongSerializer, Pha_cheSerializer, Thuong_hieuSerializer, Nuoc_hoaSerializer, BlogSerializer, GiaSerializer
from rest_framework import generics


class ListNuoc_hoa(generics.ListAPIView):
    queryset = Nuoc_hoa.objects.all()
    serializer_class = Nuoc_hoaSerializer


class DetailNuoc_hoa(generics.RetrieveAPIView):
    queryset = Nuoc_hoa.objects.all()
    serializer_class = Nuoc_hoaSerializer


class ListNhom_huong(generics.ListAPIView):
    queryset = Nhom_huong.objects.all()
    serializer_class = Nhom_huongSerializer


class DetailNhom_huong(generics.RetrieveAPIView):
    queryset = Nhom_huong.objects.all()
    serializer_class = Nhom_huongSerializer


class DetailMui_huong(generics.RetrieveAPIView):
    queryset = Mui_huong.objects.all()
    serializer_class = Mui_huongSerializer


class ListPha_che(generics.ListAPIView):
    queryset = Pha_che.objects.all()
    serializer_class = Pha_cheSerializer


class DetailPha_che(generics.RetrieveAPIView):
    queryset = Pha_che.objects.all()
    serializer_class = Pha_cheSerializer


class ListThuong_hieu(generics.ListAPIView):
    queryset = Thuong_hieu.objects.all()
    serializer_class = Thuong_hieuSerializer


class DetailThuong_hieu(generics.RetrieveAPIView):
    queryset = Thuong_hieu.objects.all()
    serializer_class = Thuong_hieuSerializer


class ListBlog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DetailBlog(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DetailImage(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class Detail_gia(generics.RetrieveAPIView):
    queryset = Gia.objects.all()
    serializer_class = GiaSerializer
