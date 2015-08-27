__author__ = 'Pamungkas Jayuda'

from rest_framework import serializers

from MASTER.models import Kecamatan, Kelurahan, Kabupaten

class KabupatenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kabupaten
        fields = (
            'nama_kabupaten',
            'keterangan'
        )


class KecamatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kecamatan
        fields = (
            'nama_kabupaten',
            'nama_kecamatan',
            'keterangan'
        )

class KelurahanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kelurahan
        fields = (
            'nama_kecamatan',
            'nama_kelurahan',
            'keterangan'
        )
