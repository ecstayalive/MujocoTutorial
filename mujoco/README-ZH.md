# Mujoco 教程
[English](./README.md)
本代码库希望能够详细的介绍机器人仿真器Mujoco。首先是因为在之后的研究生学习中，可能需要使用到该仿真器，但是Mujoco本身十分复杂，且没有一个较好的教程库，因此对给学习带来了很大的困难。其次就是希望能够通过逐步的深入了解Mujoco，不断的学习机器人相关知识提升自己的能力。当然目前，只是对Mujoco仿真器具有初步的了解。因此在此先使用markdown写一个简洁的教程，之后会随着学习不断完善。

## Mujoco
Mujoco是一个机器人仿真器，常常用于强化学习仿真。

### Mujoco c源码详解
以下是通过阅读源码得到的信息，可能有些错误。

---
**mj_loadModel(const char\* filename, int default_provider):**

- 从路径中加载xml模型，返回**model**

---
**mj_makeData(const mjModel\* m):**

- 依据模型得到模型中相关的数据**data**
- 该函数中会设置**model**的**opt**选项，其中选项内的**timestep**默认设置为$0.002$，该数值与控制频率息息相关。

---
**mj_step(const mjModel\* m, mjData\* d):**
- 该函数执行一步仿真，更新**data**中的各种数据。其中，其可以使用多种积分器求解。
- Euler（欧拉积分器），该函数调用```mj_Euler(m, d)```以实现求解。
- RK，该函数调用```mj_RungeKutta(m, d, 4)```函数进行求解。
- 上述两个求解器都有一个求解时间```step_time```。在初始化```mjv_defaultOption(&opt)```中，已经设置```timestep=0.002```，当然可以通过opt设置，这个与控制频率息息相关。

---
**mj_step1(coconst mjModel\* m, mjData\* d):**

- 在control之前调用。

---
**mj_step2(coconst mjModel\* m, mjData\* d):**

- 在control之后调用。

---
**mj_forward(const mjModel\* m, mjData\* d):**

- 该函数内部只调用了```mj_forwardSkip()```函数。
- ```mj_forwardSkip()```函数负责前向动力学与运动学计算。但是由于模型数据**data**里面有各个关节的位置，各个连杆的速度。通过该函数，可以利用**data**里面的信息获得在该时刻各个连杆的加速度和关节执行器的状态。

---



## Mujoco 原生python函数详解

### PyMujoco
一个新的mujoco的python绑定模块。

## Mujoco C++ 教程

## Mujoco Python教程