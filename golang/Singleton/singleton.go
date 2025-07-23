package Singleton

import "sync"

// Singleton 是单例模式接口定义
// 定义了单例对象应该提供的方法
type Singleton interface {
	GetConfig() *Config // 获取配置信息
	SetConfig(*Config)  // 设置配置信息
}

// singleton 是单例模式的实现结构体
// 使用小写字母开头表示不对外暴露实现细节
type singleton struct {
	config *Config // 单例对象持有的配置信息
}

// instance 保存单例实例
// once 用于确保单例只被初始化一次
var (
	instance *singleton
	once     sync.Once
)

// GetInstance 获取单例实例
// 使用sync.Once确保在多线程环境下也只创建一次实例
// 返回Singleton接口类型而不是具体实现，遵循依赖倒置原则
func GetInstance() Singleton {
	once.Do(func() {
		// 初始化单例实例，并设置默认配置
		instance = &singleton{
			config: &Config{}, // 使用空配置，实际应用中可设置默认值
		}
	})
	return instance
}

// GetConfig 获取当前配置
// 实现Singleton接口的方法
func (s *singleton) GetConfig() *Config {
	return s.config
}

// SetConfig 更新配置
// 实现Singleton接口的方法
// 注意：此方法会替换整个配置对象
func (s *singleton) SetConfig(cfg *Config) {
	s.config = cfg
}
