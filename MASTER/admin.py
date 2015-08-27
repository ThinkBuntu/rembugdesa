from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Kabupaten, Kecamatan, Kelurahan, KecamatanResource, KelurahanResource, KabupatenResource, Provinsi, ProvinsiResource, \
    DusunResource, Dusun


class ProvinsiAdmin(ImportExportModelAdmin):
    list_display = ['nama_provinsi', 'keterangan']
    resource_class = ProvinsiResource
    pass

admin.site.register(Provinsi, ProvinsiAdmin)


class KabupatenAdmin(ImportExportModelAdmin):
    list_display = ['id_provinsi','nama_kabupaten', 'keterangan']
    resource_class = KabupatenResource
    pass

admin.site.register(Kabupaten, KabupatenAdmin)


class KecamatanAdmin(ImportExportModelAdmin):
    list_display = ['id_kabupaten', 'nama_kecamatan', 'keterangan']
    resource_class = KecamatanResource
    pass

admin.site.register(Kecamatan, KecamatanAdmin)


class KelurahanAdmin(ImportExportModelAdmin):
    list_display = ['id_kecamatan', 'nama_kelurahan', 'keterangan']
    resource_class = KelurahanResource
    pass

admin.site.register(Kelurahan, KelurahanAdmin)


class DusunAdmin(ImportExportModelAdmin):
    list_display = ['id_kelurahan', 'nama_dusun', 'keterangan']
    resource_class = DusunResource
    pass

admin.site.register(Dusun, DusunAdmin)
