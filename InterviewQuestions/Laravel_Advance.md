## ✅ **Laravel Interview Questions and Answers**

---

### **1. What is Laravel? Why do you prefer it?**

**Answer:**
Laravel is a PHP web application framework that follows the MVC (Model-View-Controller) architecture. It simplifies tasks like routing, sessions, caching, authentication, and more.
I prefer Laravel because of its elegant syntax, built-in tools like **Eloquent ORM**, **Blade templating**, and **Artisan CLI**, and it makes building secure, maintainable applications much faster.

---

### **2. What is the difference between `get()` and `first()` in Eloquent?**

**Answer:**

* `get()` returns a **collection** of results (even if it’s just one).
* `first()` returns **a single model instance** (or `null` if none found).
  Use `first()` when expecting only one result.

---

### **3. What are Eloquent Relationships in Laravel? Name a few types.**

**Answer:**
Eloquent relationships define how database tables relate.
Common types:

* `hasOne`
* `hasMany`
* `belongsTo`
* `belongsToMany`
* `hasManyThrough`

Example:

```php
public function posts() {
    return $this->hasMany(Post::class);
}
```

---

### **4. What are migrations in Laravel?**

**Answer:**
Migrations are version control for your database schema. They allow you to define table structure in code and share schema changes easily.

```bash
php artisan make:migration create_users_table
php artisan migrate
```

---

### **5. What is a seeder and factory in Laravel?**

**Answer:**

* **Seeders** populate the database with static or test data.
* **Factories** are used with seeders to generate fake data using the Faker library.

```php
User::factory()->count(10)->create();
```

---

### **6. What is middleware in Laravel?**

**Answer:**
Middleware filters HTTP requests entering your application.
For example, `auth` middleware ensures that only logged-in users can access certain routes.

```php
Route::get('/dashboard', function () {
    // ...
})->middleware('auth');
```

---

### **7. How does Laravel handle authentication?**

**Answer:**
Laravel offers built-in solutions:

* Laravel Breeze (lightweight)
* Laravel Jetstream (full-featured with 2FA)
  It includes user registration, login, password reset, and session management using guards and providers defined in `config/auth.php`.

---

### **8. What is CSRF protection in Laravel?**

**Answer:**
CSRF (Cross-Site Request Forgery) protection prevents unauthorized commands.
Laravel includes CSRF tokens in forms using:

```blade
@csrf
```

It validates the token on POST/PUT/DELETE requests.

---

### **9. What is the difference between `include` and `extends` in Blade?**

**Answer:**

* `@extends` is used for layout inheritance.
* `@include` is used to insert reusable Blade partials.

---

### **10. How do you create and use a custom Artisan command?**

**Answer:**

```bash
php artisan make:command MyCustomCommand
```

Inside the command file, define the logic in `handle()`, and register it in `Kernel.php`.

---

### **11. What are queues in Laravel and when do you use them?**

**Answer:**
Queues are used to defer time-consuming tasks like email sending or data processing to improve performance.
Laravel supports multiple queue drivers like `database`, `redis`, and `sqs`.

---

### **12. What are service providers in Laravel?**

**Answer:**
Service providers are the central place to configure and bind classes into Laravel's service container.
Every Laravel app has many providers listed in `config/app.php`.

---

### **13. How do you validate a request in Laravel?**

**Answer:**

```php
$request->validate([
    'email' => 'required|email',
    'password' => 'required|min:6',
]);
```

Alternatively, use **Form Request** classes.

---

### **14. What are some security features in Laravel?**

**Answer:**

* CSRF Protection
* Password Hashing (bcrypt, argon2)
* XSS Protection with Blade escaping
* SQL Injection protection via Eloquent/Query Builder
* HTTPS enforcement (manually via middleware)

---

### **15. What’s the difference between Laravel’s Query Builder and Eloquent?**

**Answer:**

* **Query Builder** is a fluent, lower-level interface to run database queries.
* **Eloquent** is Laravel’s ORM that uses model classes for table operations.

---

## ✅ **Advanced Laravel Interview Questions and Answers**

---

### **16. What is the Repository Pattern in Laravel? Why use it?**

**Answer:**
The Repository Pattern separates the logic that retrieves data from the database from the business logic.
It improves code **reusability, testability, and maintenance**.

```php
interface UserRepositoryInterface {
    public function getAllUsers();
}

class UserRepository implements UserRepositoryInterface {
    public function getAllUsers() {
        return User::all();
    }
}
```

---

### **17. How do you handle file uploads in Laravel?**

**Answer:**

```php
public function store(Request $request) {
    $path = $request->file('image')->store('images');
}
```

You can also validate:

```php
$request->validate([
    'image' => 'required|image|mimes:jpg,png|max:2048'
]);
```

---

### **18. What are Events and Listeners in Laravel?**

**Answer:**
Events allow you to hook into specific points in your app.
Listeners handle the logic when the event is fired.
Used for things like logging, sending emails, notifications, etc.

```bash
php artisan make:event UserRegistered
php artisan make:listener SendWelcomeEmail
```

---

### **19. How do you use Laravel Task Scheduling?**

**Answer:**
Define scheduled jobs in `App\Console\Kernel.php` using `schedule()` method.

```php
$schedule->command('emails:send')->daily();
```

And then run:

```bash
* * * * * php /path/to/artisan schedule:run >> /dev/null 2>&1
```

---

### **20. What is Laravel Sanctum?**

**Answer:**
Sanctum is Laravel’s lightweight API authentication system for:

* SPAs (Single Page Applications)
* Mobile Apps
* Simple token-based APIs

It supports **token authentication** without OAuth complexity.

---

### **21. How do you implement soft deletes in Laravel?**

**Answer:**

```php
use Illuminate\Database\Eloquent\SoftDeletes;

class Post extends Model {
    use SoftDeletes;
}
```

This adds a `deleted_at` column and allows you to:

* `Post::withTrashed()`
* `Post::onlyTrashed()`
* `Post::restore()`

---

### **22. How can you optimize performance in a Laravel app?**

**Answer:**

* Use **Eager Loading** to avoid N+1 query problems.
* Cache queries using Laravel Cache.
* Use queues for emails & background jobs.
* Optimize database indexes and queries.
* Use `php artisan config:cache`, `route:cache`, `view:cache`.

---

### **23. What are service containers and bindings in Laravel?**

**Answer:**
The **service container** is Laravel’s dependency injection container.

You can bind interfaces to implementations:

```php
App::bind('App\Repositories\UserRepositoryInterface', function ($app) {
    return new UserRepository();
});
```

---

### **24. How do you create custom middleware?**

**Answer:**

```bash
php artisan make:middleware CheckUserRole
```

Inside:

```php
if ($request->user()->role != 'admin') {
    return redirect('home');
}
```

Register it in `Kernel.php`.

---

### **25. What is rate limiting in Laravel?**

**Answer:**
Laravel allows rate-limiting APIs to avoid abuse:

```php
Route::middleware(['throttle:60,1'])->group(function () {
    // routes here
});
```

This allows 60 requests per 1 minute.

---

### **26. How do you write unit tests in Laravel?**

**Answer:**

```bash
php artisan make:test UserTest
```

Inside:

```php
public function test_user_can_be_created() {
    $response = $this->post('/users', [
        'name' => 'John',
        'email' => 'john@example.com'
    ]);
    $response->assertStatus(200);
}
```

---

### **27. What is the difference between `hasOne` and `belongsTo`?**

**Answer:**

* `hasOne`: The current model owns one of the related model.
* `belongsTo`: The current model is a child of the related model.

Example:

```php
// User.php
public function profile() {
    return $this->hasOne(Profile::class);
}

// Profile.php
public function user() {
    return $this->belongsTo(User::class);
}
```

---

### **28. How does Laravel handle localization?**

**Answer:**
Laravel uses the `resources/lang` directory.
You can set the language:

```php
App::setLocale('fr');
```

And create translation files like `fr/messages.php` and access using:

```php
__('messages.welcome')
```

---

### **29. How do you debug in Laravel?**

**Answer:**

* `dd()`, `dump()`, and `Log::info()`
* Laravel Debugbar (package)
* Laravel Telescope (advanced debugging tool)

---

### **30. How to protect routes using middleware and guards?**

**Answer:**
In routes/web.php:

```php
Route::middleware(['auth'])->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index']);
});
```

In `config/auth.php`, define guards for web, API, etc.

---