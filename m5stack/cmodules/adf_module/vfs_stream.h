/*
 * ESPRESSIF MIT License
 *
 * Copyright (c) 2019 <ESPRESSIF SYSTEMS (SHANGHAI) CO., LTD>
 * Copyright (c) 2024 M5Stack Technology CO LTD
 *
 * Permission is hereby granted for use on all ESPRESSIF SYSTEMS products, in which case,
 * it is free of charge, to any person obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the Software is furnished
 * to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 */

#ifndef VFS_STREAM_H_
#define VFS_STREAM_H_

#include "audio_element.h"

// #ifdef __cplusplus
// extern "C" {
// #endif

/**
 * @brief   FATFS Stream configurations, if any entry is zero then the configuration will be set to default values
 */
typedef struct {
    audio_stream_type_t type; /*!< Stream type */
    int buf_sz;               /*!< Audio Element Buffer size */
    int out_rb_size;          /*!< Size of output ringbuffer */
    int task_stack;           /*!< Task stack size */
    int task_core;            /*!< Task running in core (0 or 1) */
    int task_prio;            /*!< Task priority (based on freeRTOS priority) */
} vfs_stream_cfg_t;

#define VFS_STREAM_BUF_SIZE (2048)
#define VFS_STREAM_TASK_STACK (3072)
#define VFS_STREAM_TASK_CORE (0)
#define VFS_STREAM_TASK_PRIO (4)
#define VFS_STREAM_RINGBUFFER_SIZE (8 * 1024)

#define VFS_STREAM_CFG_DEFAULT()               \
    {                                              \
        .type = AUDIO_STREAM_NONE,                \
        .buf_sz = VFS_STREAM_BUF_SIZE,             \
        .out_rb_size = VFS_STREAM_RINGBUFFER_SIZE, \
        .task_stack = VFS_STREAM_TASK_STACK,       \
        .task_core = VFS_STREAM_TASK_CORE,         \
        .task_prio = VFS_STREAM_TASK_PRIO,         \
    }

/**
 * @brief      Create a handle to an Audio Element to stream data from FatFs to another Element
 *             or get data from other elements written to FatFs, depending on the configuration
 *             the stream type, either AUDIO_STREAM_READER or AUDIO_STREAM_WRITER.
 *
 * @param      config  The configuration
 *
 * @return     The Audio Element handle
 */
audio_element_handle_t vfs_stream_init(vfs_stream_cfg_t *config);

// #ifdef __cplusplus
// }
// #endif

#endif
