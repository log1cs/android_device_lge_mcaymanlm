#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/lge/mcaymanlm

# Kernel
TARGET_KERNEL_CONFIG := lineageos_mcaymanlm_defconfig

# Inherit the proprietary files
include vendor/lge/mcaymanlm/BoardConfigVendor.mk
