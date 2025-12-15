#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Indicate the first API level the device has been commercially launched on
PRODUCT_SHIPPING_API_LEVEL := 29

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from device makefile
$(call inherit-product, $(LOCAL_PATH)/device.mk)

PRODUCT_NAME := lineage_mcaymanlm
PRODUCT_DEVICE := mcaymanlm
PRODUCT_MANUFACTURER := lge
PRODUCT_BRAND := LGE
PRODUCT_MODEL := LM-G900TM

PRODUCT_GMS_CLIENTID_BASE := android-lge

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="mcaymanlm-user 11 RKQ1.210420.001 221041357a1fb release-keys" \
    BuildFingerprint=lge/mcaymanlm/mcaymanlm:11/RKQ1.210420.001/221041357a1fb:user/release-keys \
    DeviceName=mcaymanlm \
    DeviceProduct=mcaymanlm \
    SystemDevice=mcaymanlm \
    SystemName=mcaymanlm
