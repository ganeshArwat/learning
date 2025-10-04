Here are some **Laravel Fundamental Interview Questions** to help you prepare:

---

### 🔹 **Basic Laravel Questions**

1. **What is Laravel?**

   * Laravel is a PHP framework used for developing web applications following the MVC (Model-View-Controller) architectural pattern.

2. **What are the main features of Laravel?**

   * Artisan CLI
   * Eloquent ORM
   * Blade templating engine
   * Routing
   * Middleware
   * Migrations & Seeders
   * Authentication & Authorization
   * Queues & Jobs
   * Events & Listeners

3. **What is MVC in Laravel?**

   * MVC stands for Model-View-Controller. It separates application logic (Controller), data (Model), and UI (View).

4. **What is Artisan in Laravel?**

   * Artisan is Laravel’s command-line interface to automate tasks like generating files, running migrations, and clearing cache.

5. **What is Eloquent ORM?**

   * Eloquent is Laravel’s built-in Object-Relational Mapping (ORM) tool for interacting with the database using models.

---

### 🔹 **Routing & Middleware**

6. **What is routing in Laravel?**

   * Routing is how Laravel handles incoming requests and maps them to controllers or closures.

7. **What is a middleware?**

   * Middleware filters HTTP requests before they reach the controller. Example: `auth`, `csrf`, `cors`.

8. **How to create a middleware in Laravel?**

   ```
   php artisan make:middleware CheckAge
   ```

9. **What are route types in Laravel?**

   * Basic Route
   * Route with Parameters
   * Named Routes
   * Route Groups
   * Route Resource

---

### 🔹 **Controllers & Views**

10. **How to create a controller in Laravel?**

```
php artisan make:controller PostController
```

11. **What is the use of Blade in Laravel?**

* Blade is Laravel’s templating engine used for writing clean and reusable view code.

12. **How to pass data from controller to view?**

```php
return view('home', ['name' => 'Ganesh']);
```

---

### 🔹 **Models & Migrations**

13. **How to create a model with a migration?**

```
php artisan make:model Product -m
```

14. **What is a migration in Laravel?**

* Migrations are version control for your database, allowing you to create, modify, and share schemas.

15. **How to run migrations?**

```
php artisan migrate
```

16. **What is the difference between `softDelete` and `delete` in Laravel?**

* `delete()` removes data permanently.
* `softDelete()` flags it as deleted but keeps it in the DB.

---

### 🔹 **Database & Eloquent**

17. **What is the difference between `hasOne` and `belongsTo`?**

* `hasOne` defines a one-to-one relationship from parent to child.
* `belongsTo` defines a relationship from child to parent.

18. **How to use Eloquent relationships?**

* `hasOne`, `hasMany`, `belongsTo`, `belongsToMany`, `morphOne`, `morphMany`, etc.

19. **What are accessors and mutators in Laravel?**

* Accessor: Format data when retrieving it from DB.
* Mutator: Format data before saving it to DB.

---

### 🔹 **Authentication & Validation**

20. **How does Laravel handle authentication?**

* Laravel provides built-in authentication scaffolding using Breeze, Jetstream, or Fortify.

21. **How to validate form data in Laravel?**

```php
$request->validate([
    'email' => 'required|email',
    'password' => 'required|min:6'
]);
```

---

### 🔹 **Other Common Questions**

22. **What is CSRF Token in Laravel?**

* CSRF (Cross-Site Request Forgery) token is a security feature to prevent unauthorized actions from other sites.

23. **What is service provider in Laravel?**

* Service providers are the central place of Laravel bootstrapping and dependency injection.

24. **What is the use of `config/app.php`?**

* It contains app-specific configuration like timezone, locale, service providers, aliases, etc.

25. **What is the difference between `include`, `require`, and `@include` in Laravel Blade?**

* `@include` is a Blade directive for including views.

---

### 🔸 **Advanced Routing**

1. **What is route model binding in Laravel?**

   * Laravel automatically injects the model instance based on the route parameter.

   ```php
   Route::get('/user/{user}', function (App\Models\User $user) {
       return $user;
   });
   ```

2. **What is the difference between `Route::get` and `Route::resource`?**

   * `Route::get` defines individual routes.
   * `Route::resource` creates all CRUD routes for a controller.

3. **How to handle 404 errors in Laravel?**

   * By using `abort(404)` or customizing the `resources/views/errors/404.blade.php` file.

---

### 🔸 **Request Lifecycle & Dependency Injection**

4. **Explain Laravel's request lifecycle.**

   * `public/index.php` → `App\Http\Kernel` → Middleware → Routes → Controllers → Response

5. **What is dependency injection in Laravel?**

   * Laravel automatically injects class dependencies in constructors or methods using the service container.

---

### 🔸 **Eloquent & Relationships**

6. **How to eager load relationships in Laravel?**

   ```php
   User::with('posts')->get();
   ```

7. **What is the difference between `pluck()` and `select()` in Eloquent?**

   * `pluck()` retrieves a single column as an array.
   * `select()` builds a query to retrieve specific columns but returns full models.

8. **What is a pivot table in Laravel?**

   * A pivot table is used in `belongsToMany` relationships to store the relationship between two models.

---

### 🔸 **Authentication & Authorization**

9. **What is Laravel Sanctum and Passport?**

   * Sanctum: Lightweight API token authentication for SPAs and mobile apps.
   * Passport: Full OAuth2 server for more complex needs.

10. **What is the difference between `Auth::check()` and `Auth::user()`?**

* `Auth::check()` returns `true/false` if the user is logged in.
* `Auth::user()` returns the authenticated user object.

---

### 🔸 **Artisan & Console**

11. **How to create a custom Artisan command?**

```
php artisan make:command SendEmailReport
```

12. **How to schedule tasks in Laravel?**

* Use the `schedule()` method in `App\Console\Kernel`.

```php
protected function schedule(Schedule $schedule)
{
    $schedule->command('emails:send')->daily();
}
```

---

### 🔸 **Events, Listeners, and Queues**

13. **What are events and listeners in Laravel?**

* Events allow you to hook into and react to various parts of your application.
* Listeners handle the logic when an event is fired.

14. **What are queues in Laravel?**

* Queues allow you to defer time-consuming tasks (emails, jobs) to be processed later.

```bash
php artisan queue:work
```

15. **How to create a queued job?**

```
php artisan make:job SendWelcomeEmail
```

---

### 🔸 **Testing**

16. **What testing tools does Laravel provide?**

* Laravel uses PHPUnit and has a rich set of testing features like `feature` and `unit` tests.

17. **How to write a feature test in Laravel?**

```
php artisan make:test UserLoginTest
```

---

### 🔸 **Miscellaneous**

18. **What is the `service container` in Laravel?**

* It is a powerful tool for managing class dependencies and performing dependency injection.

19. **What is a facade in Laravel?**

* Facades provide a "static" interface to classes in the service container. Example: `Route`, `DB`, `Cache`, `Auth`.

20. **What is `config:cache` and why do we use it?**

* It caches all config files to a single file to boost performance.

---


