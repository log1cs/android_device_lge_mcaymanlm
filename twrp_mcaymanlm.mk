#
# Copyright (C) 2026 The Android Open Source Project
# Copyright (C) 2026 SebaUbuntu's TWRP device tree generator
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Omni stuff.
$(call inherit-product, vendor/twrp/config/common.mk)

# Inherit from mcaymanlm device
$(call inherit-product, device/lge/mcaymanlm/device.mk)

PRODUCT_DEVICE := mcaymanlm
PRODUCT_NAME := twrp_mcaymanlm
PRODUCT_BRAND := lge
PRODUCT_MODEL := VELVET
PRODUCT_MANUFACTURER := lge

PRODUCT_GMS_CLIENTID_BASE := android-lge

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="mcaymanlm-user 11 RKQ1.210420.001 221041357a1fb release-keys"

BUILD_FINGERPRINT := lge/mcaymanlm/mcaymanlm:11/RKQ1.210420.001/221041357a1fb:user/release-keys
