package Singleton

import "fmt"

func Demo() {
	// 演示单例模式的基本特性

	// 第一次获取单例实例
	instance1 := GetInstance()
	// 第二次获取单例实例
	instance2 := GetInstance()

	// 打印两个实例的内存地址
	// 预期结果：地址相同，证明是同一个实例
	fmt.Printf("instance1 地址: %p\n", instance1)
	fmt.Printf("instance2 地址: %p\n", instance2)

	// 直接比较两个实例
	fmt.Println("是否是同一个实例？", instance1 == instance2)

	// 演示单例对象的数据共享特性

	// 创建一个新的配置对象
	cfg := NewConfig()
	// 修改配置值
	cfg.AppName = "SingletonDemo" // 设置应用名称
	cfg.DebugMode = true          // 启动调试模式

	// 通过instance1 设置配置
	instance1.SetConfig(cfg)

	// 通过instance2获取配置
	fmt.Println("\n通过instance2获取配置:")
	fmt.Println("AppName:", instance2.GetConfig().AppName)
	fmt.Println("DebugMode:", instance2.GetConfig().DebugMode)

	// 演示配置的共享特性

	// 通过instance2修改数据库端口
	instance2.GetConfig().Database.Port = 5432 // 修改为PostgresSQL

	// 通过instance1检查修改
	// 预期结果：能看到通过instance2做的修改
	fmt.Println("\n通过instance1检查数据库端口:")
	fmt.Println("Database Port:", instance1.GetConfig().Database.Port)

	// 典型应用场景说明：
	// 1. 全局配置管理
	// 2. 数据库连接池
	// 3. 日志记录器
	// 4. 应用缓存
	// 5. 其他需要全局唯一实例的场景

}
