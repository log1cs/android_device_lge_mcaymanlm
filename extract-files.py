#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/lge/mcaymanlm',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client'
]

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-mtk.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-mtk.so')
        .replace_needed('libcodec2_hidl@1.2.so', 'libcodec2_hidl@1.2-mtk.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so'),
    'vendor/lib/hw/audio.primary.mt6885.so': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libalsautils.so', 'libalsautils-mtk.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib/librt_extamp_intf.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    ('vendor/lib64/libets_trustlet.so', 'vendor/lib64/libfpsph.so'): blob_fixup()
        .add_needed('libets_teeclient_v2_shim.so'),
    'vendor/lib64/hw/sensors.mt6885.so': blob_fixup()
        .fix_soname()
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libcodec2_hidl@1.0-mtk.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-mtk.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-mtk.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.1-mtk.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-mtk.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-mtk.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-mtk.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.2-mtk.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-mtk.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-mtk.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-mtk.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-mtk.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl_plugin-mtk.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so'),
    ('vendor/lib64/libcodec2_mtk_c2store.so', 'vendor/lib64/libcodec2_vpp_qt_plugin.so', 'vendor/lib64/libcodec2_vpp_rs_plugin.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-mtk.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-mtk.so'),
    ('vendor/lib64/libcodec2_mtk_vdec.so', 'vendor/lib64/libcodec2_mtk_venc.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-mtk.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-mtk.so')
        .replace_needed('libui.so', 'libui-v34.so'),
    'vendor/lib64/libcodec2_soft_common-mtk.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-mtk.so'),
    'vendor/lib64/libcodec2_vndk-mtk.so': blob_fixup()
        .replace_needed('libui.so', 'libui-v34.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libsfplugin_ccodec_utils-mtk.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-mtk.so'),
}  # fmt: skip


module = ExtractUtilsModule(
    'mcaymanlm',
    'lge',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
