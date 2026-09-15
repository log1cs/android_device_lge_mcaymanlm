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
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/lge/mcaymanlm',
    'hardware/lge',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client'
]

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libims.lge.so': blob_fixup()
        .add_needed('libmtkutils.so'),
    'system_ext/lib64/libimsmmpf.lge.so': blob_fixup()
        .add_needed('libgui_buffer_shim_vendor.so')
        .add_needed('libui_shim.so'),
    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/bin/mnld': blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so')
        .replace_needed('libmnl.so', 'libmnl_mtk.so'),
    'vendor/lib/hw/audio.primary.mt6885.so': blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-mtk.so'),
    'vendor/lib/libMtkOmxVdecEx.so': blob_fixup()
        .add_needed('libui_shim.so'),
    ('vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/sensors.mt6885.so': blob_fixup()
        .fix_soname()
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    ('vendor/lib64/lib3a.flash.so', 'vendor/lib64/lib3a.ae.stat.so', 'vendor/lib64/libaaa_ltm.so'): blob_fixup()
        .add_needed('liblog.so'),
    ('vendor/lib64/libaalservice.so', 'vendor/lib64/libcam.utils.sensorprovider.so', 'vendor/lib64/librgbwlightsensor.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    'vendor/lib/libmnl_mtk.so': blob_fixup()
        .add_needed('libcutils.so'),
    ('vendor/lib64/mediadrm/libwvdrmengine.so', 'vendor/lib64/libwvhidl.so'): blob_fixup()
        .add_needed('libcrypto_shim.so'),
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
