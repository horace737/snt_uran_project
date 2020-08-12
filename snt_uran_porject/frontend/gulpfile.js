'use strict';

var gulp = require('gulp'),

    // main
    rename = require('gulp-rename'),

    // css
    less = require('gulp-less'),
    cssnano = require('gulp-cssnano'),
    autoprefixer = require('gulp-autoprefixer'),

    // js
    uglify = require('gulp-uglify'),
    babel = require('gulp-babel');


// open settings.json
try {
    var settings = require('./settings'); // remove 1
} catch (error) {
    if (error.code !== 'MODULE_NOT_FOUND') {
        throw error;
    }
    settings = {
        "build" : "build/"
    }
}


gulp.task('style', function() {
    gulp.src('src/less/style.less')
    .pipe(less())
    .pipe(autoprefixer([
        'last 15 versions', '> 1%', 'ie 8', 'ie 7'
        ]))
    .pipe(cssnano())
    .pipe(rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest(settings.build + 'css'))
});


gulp.task('js', function() {
    gulp.src('src/js/common.js')
    .pipe(babel({
        "presets": ["env"]
    }))
    .pipe(uglify())
    .pipe(rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest(settings.build + 'js'));

//copy plugins
    return gulp.src('src/js/plugins/**')
    .pipe(gulp.dest(settings.build + 'js'));
});

gulp.task('img', function() {
    return gulp.src('src/img/**')
    .pipe(gulp.dest(settings.build + 'img'));
});


gulp.task('watch', function() {
    gulp.watch('src/less/**/*.less', ['style']);
    gulp.watch('src/js/**/*.js', ['js']);
    gulp.watch('src/img/**/*.jpg', ['img']);
});


gulp.task('default', ['watch']);