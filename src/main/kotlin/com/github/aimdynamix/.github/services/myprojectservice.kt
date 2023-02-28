package com.github.aimdynamix.github.services

import com.intellij.openapi.project.Project
import com.github.aimdynamix.github.MyBundle

class MyProjectService(project: Project) {

    init {
        println(MyBundle.message("projectService", project.name))
    }
}
