<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Http;

class AuthController extends Controller
{
    public function showLoginForm()
    {
        return view('login');
    }

    public function login(Request $request)
    {
        // dd('lolll');

        $credentials = $request->validate([
            'email' => ['required'],
            'password' => ['required'],
        ]);

        dump($credentials);
        // if (Auth::attempt($credentials)) {
            // $request->session()->regenerate();
            $response = Http::withHeaders([
                'Content-Type' => 'application/json',
            ])->post('http://localhost:8000/api/utilisateur/connexion/', [
                'username' => $credentials['email'],
                'password' => $credentials['password'],
            ]);

            $request->session()->put('djangoSession', $response->json());
            dump($response->json());

            return redirect('/');
        // }

        return back()->withErrors([
            'email' => 'The provided credentials do not match our records.',
        ]);
    }

    public function logout(Request $request)
    {
        Auth::logout();

        $request->session()->invalidate();

        $request->session()->regenerateToken();

        return redirect('/');
    }
}
