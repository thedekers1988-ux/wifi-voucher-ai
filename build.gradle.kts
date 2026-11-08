plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
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
