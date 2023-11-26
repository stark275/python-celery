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

        $credentials = $request->validate([
            'email' => ['required'],
        ]);

        // if (Auth::attempt($credentials)) {
            // $request->session()->regenerate();
            $response = Http::withHeaders([
                'Content-Type' => 'application/json',
            ])->post('http://localhost:8000/api/utilisateur/connexion/', [
                'username' => $credentials['email'],
            ]);

            $request->session()->put('djangoSession', $response->json());

            return redirect('/');
        // }

        return back()->withErrors([
            'email' => 'The provided credentials do not match our records.',
        ]);
    }

    public function logout(Request $request)
    {



        // Auth::logout();
        // $request->session()->invalidate();
        // $request->session()->regenerateToken();
        // dd(session('djangoSession'));

        try {
            // Supprimer la session
            $response = Http::withHeaders([
                'Content-Type' => 'application/json',
            ])->post('http://localhost:8000/api/utilisateur/logout/',
                [
                    'csrfmiddlewaretoken' => session('djangoSession')['csrftoken'],
                    'sessionid' => session('djangoSession')['sessionid'],
                ]
            );

            // Vérifier si la requête a réussi
            if ($response->ok()) {
                $request->session()->forget('djangoSession');
                return redirect()->route('login');

            } else {
                echo "Erreur lors de la destruction de la session. Code d'erreur : " . $response->status();
            }
        } catch (\Exception $e) {
            echo "Une erreur s'est produite lors de la destruction de la session : " . $e->getMessage();
        }

    }
}
