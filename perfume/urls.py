from django.urls import path
from .views import ListNuoc_hoa, DetailNuoc_hoa, DetailImage, ListBlog, DetailBlog, ListNhom_huong, DetailNhom_huong, DetailMui_huong, ListThuong_hieu, DetailThuong_hieu, ListPha_che, DetailPha_che, Detail_gia


urlpatterns = [
    path('', ListNuoc_hoa.as_view(), name='list_nuoc_hoa'),
    path('<int:pk>/', DetailNuoc_hoa.as_view(), name='detail_nuoc_hoa'),
    path('image/<int:pk>/', DetailImage.as_view(), name='detail_image'),
    path('blog/', ListBlog.as_view(), name='list_blog'),
    path('blog/<int:pk>/', DetailBlog.as_view(), name='detail_blog'),
    path('nhom_huong/', ListNhom_huong.as_view(), name='list_nhom_huong'),
    path('nhom_huong/<int:pk>/', DetailNhom_huong.as_view(), name='detail_nhom_huong'),
    path('mui_huong/<int:pk>/', DetailMui_huong.as_view(), name='detail_mui_huong'),
    path('pha_che/', ListPha_che.as_view(), name='list_pha_che'),
    path('pha_che/<int:pk>/', DetailPha_che.as_view(), name='detail_pha_che'),
    path('thuong_hieu/', ListThuong_hieu.as_view(), name='list_thuong_hieu'),
    path('thuong_hieu/<int:pk>/', DetailThuong_hieu.as_view(), name='detail_thuong_hieu'),
    path('gia/<int:pk>/', Detail_gia.as_view(), name='detail_gia'),
]
