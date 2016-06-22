var gulp = require('gulp');
const del = require('del');
const typescript = require('gulp-typescript');
const tscConfig = require('./tsconfig.json');
const sourcemaps = require('gulp-sourcemaps');

const appPath = 'ui/static/'


gulp.task('clean', function () {
  return del(appPath + 'dist/**/*');
});


gulp.task('compile', ['clean'], function () {
   return gulp
    .src(['typings/browser.d.ts', appPath + 'app/**/*.ts'])
    .pipe(sourcemaps.init())
    .pipe(typescript(tscConfig.compilerOptions))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(appPath + 'dist'));
});


gulp.task('tslint', function() {
  var tslint = require('gulp-tslint');
  return gulp.src(appPath + 'app/**/*.ts')
    .pipe(tslint())
    .pipe(tslint.report('verbose'));
});


gulp.task("libs", function () {
    return gulp.src([
        'es6-shim/es6-shim.min.js',
        'systemjs/dist/system-polyfills.js',
        'systemjs/dist/system.src.js',
        'reflect-metadata/Reflect.js',
        'raven-js/dist/**',
        'rxjs/**',
        'zone.js/dist/**',
        '@angular/common/common.umd.js',
        '@angular/compiler/compiler.umd.js',
        '@angular/core/core.umd.js',
        '@angular/http/http.umd.js',
        '@angular/platform-browser/platform-browser.umd.js',
        '@angular/platform-browser-dynamic/platform-browser-dynamic.umd.js',
        '@angular/router-deprecated/router-deprecated.umd.js',
        '@angular/upgrade/upgrade.umd.js',
        'bootstrap/dist/**',
        'jquery/dist/**'
    ], {cwd: "node_modules/**"}) /* Glob required here. */
    .pipe(gulp.dest(appPath + "lib/"));
});


gulp.task("dev_libs", function () {
    return gulp.src([
        'jasmine-core/lib/jasmine-core/jasmine.css',
        'jasmine-core/lib/jasmine-core/jasmine.js',
        'jasmine-core/lib/jasmine-core/jasmine-html.js',
        'jasmine-core/lib/jasmine-core/boot.js'
    ], {cwd: "node_modules/**"}) /* Glob required here. */
    .pipe(gulp.dest(appPath + "lib/"));
});


gulp.task('default', function() {
  gulp.start('compile', 'libs');
});
