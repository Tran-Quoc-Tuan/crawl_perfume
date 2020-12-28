from rest_framework import serializers
from .models import Image, Nhom_huong, Mui_huong, Pha_che, Thuong_hieu, Nuoc_hoa, Gia, Blog


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = [
            'ten', 'image.url',
        ]


class Nhom_huongSerializer(serializers.HyperlinkedModelSerializer):
    image_mui_huong = serializers.HyperlinkedRelatedField(
        read_only=True, view_name= 'detail_mui_huong'
    )
    image = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_image'
    )

    class Meta:
        model = Nhom_huong
        fields = [
            'id', 'ten', 'mo_ta', 'image', 'image_mui_huong',
        ]


class Mui_huongSerializer(serializers.HyperlinkedModelSerializer):
    nhom_mui = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_nhom_huong'
    )
    image = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='detail_image'
    )
    nuoc_hoa = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_nuoc_hoa'
    )

    class Meta:
        model = Mui_huong
        fields = [
            'id', 'nhom_mui', 'mo_ta', 'image', 'nuoc_hoa',
        ]


class Pha_cheSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_image'
    )
    nuoc_hoa = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_nuoc_hoa'
    )

    class Meta:
        model = Pha_che
        fields = [
            'id', 'ten', 'gioi_thieu', 'image', 'nuoc_hoa',
        ]


class Thuong_hieuSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_image'
    )
    nuoc_hoa = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_nuoc_hoa'
    )

    class Meta:
        model = Thuong_hieu
        fields = [
            'id', 'country', 'gioi_thieu', 'website', 'nuoc_hoa',
        ]


class Nuoc_hoaSerializer(serializers.HyperlinkedModelSerializer):
    thuong_hieu = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_thuong_hieu'
    )
    pha_che = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_pha_che'
    )
    huong_dau = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_mui_huong'
    )
    huong_chinh = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_mui_huong'
    )
    huong_cuoi = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_mui_huong'
    )
    image = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_image'
    )
    nuoc_hoa = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='detail_gia'
    )

    class Meta:
        model = Nuoc_hoa
        fields = [
            'id', 'ten', 'thuong_hieu', 'nhom_nuoc_hoa', 'gioi_tinh', 'do_tuoi', 'nam_sx', 'nong_do', 'pha_che',
            'do_luu', 'do_toa', 'khuyen_dung', 'phong_cach', 'huong_dau', 'huong_chinh', 'huong_cuoi', 'diem', 'tong_quan',
            'chi_tiet', 'image', 'nuoc_hoa',
        ]


class GiaSerializer(serializers.HyperlinkedModelSerializer):
    nuoc_hoa = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='detail_nuoc_hoa'
    )

    class Meta:
        model = Gia
        fields =[
            'nuoc_hoa', 'gia', 'dia_diem',
        ]


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'date_create', 'content',
        ]
