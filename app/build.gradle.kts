plugins {
    id("com.android.application") version "8.7.3"
    id("org.jetbrains.kotlin.android") version "2.0.21"
}

android {
    namespace = "id.wifivoucher.ai"
    compileSdk = 35

    defaultConfig {
        applicationId = "id.wifivoucher.ai"
        minSdk = 23
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }
}
