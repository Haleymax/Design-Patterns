package Singleton

// Config 表示应用程序的配置结构
// 作为单例模式中管理的共享数据示例
type Config struct {
	AppName    string // 应用程序名
	AppVersion string // 应用程序版本
	DebugMode  bool   // 是否调试模式

	// 嵌套结构体，表示数据库配置
	Database struct {
		Host     string // 数据库主机
		Port     int    // 数据库端口
		Username string // 数据库用户名
		Password string // 数据库密码
	}
}

func NewConfig() *Config {
	// 初始化配置对象
	cfg := &Config{
		AppName:    "MyApp", // 默认应用名称
		AppVersion: "1.0.0", // 默认版本号
		DebugMode:  false,   // 默认非调试模式
	}

	// 设置数据库默认配置
	cfg.Database.Host = "localhost"  // 默认本地主机
	cfg.Database.Port = 3306         // 默认MySQL端口
	cfg.Database.Username = "root"   // 默认用户名
	cfg.Database.Password = "123456" // 默认密码

	return cfg
}
