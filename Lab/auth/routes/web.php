<?php

use App\Http\Controllers\AuthController;
use Illuminate\Support\Facades\Route;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/login',[AuthController::class, 'showLoginForm'])->name('login');
Route::post('/login',[AuthController::class, 'login'])->name('login.attempt');
Route::post('/logout',[AuthController::class, 'logout'])->name('logout');

Route::get('/', function () {

    // dd(session('djangoSession'));

    return view('welcome', [
        'djangoSession' => session('djangoSession'),
    ]);
});
