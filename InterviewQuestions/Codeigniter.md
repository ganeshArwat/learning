## ✅ **CodeIgniter Interview Questions & Answers**

---

### **1. What is CodeIgniter?**

CodeIgniter is a lightweight and powerful **PHP framework** that uses the **MVC (Model-View-Controller)** pattern to organize and separate application logic from the user interface. It’s known for being fast, small in footprint, and easy to learn.

---

### **2. What is MVC in CodeIgniter?**

* **Model** – Handles data and business logic.
* **View** – Handles user interface (HTML/CSS/JS).
* **Controller** – Acts as a mediator between Model and View.

```plaintext
User → Controller → Model → Database → Model → Controller → View → Output
```

---

### **3. How does routing work in CodeIgniter?**

Routing defines how URL requests are mapped to controllers and methods.

**Default route:** Defined in `application/config/routes.php`

```php
$route['default_controller'] = 'Welcome';
$route['404_override'] = '';
$route['translate_uri_dashes'] = FALSE;
```

**Custom route:**

```php
$route['profile/(:num)'] = 'user/profile/$1';
```

---

### **4. How do you load a model, view, and controller in CodeIgniter?**

**Load model in controller:**

```php
$this->load->model('User_model');
```

**Load view:**

```php
$this->load->view('home');
```

---

### **5. How to use the database in CodeIgniter?**

**Active Record (Query Builder) example:**

```php
$this->db->select('*')->from('users')->where('id', 1)->get()->result();
```

**Insert:**

```php
$data = ['name' => 'Ganesh'];
$this->db->insert('users', $data);
```

**Update:**

```php
$this->db->where('id', 1)->update('users', ['name' => 'Updated']);
```

---

### **6. What are helpers and libraries in CodeIgniter?**

* **Helpers** = Group of procedural functions (e.g., `url_helper`, `form_helper`).

  ```php
  $this->load->helper('url');
  echo base_url();
  ```

* **Libraries** = Class-based functionality (e.g., `session`, `email`, `form_validation`).

  ```php
  $this->load->library('session');
  ```

---

### **7. How do you handle form validation in CodeIgniter?**

```php
$this->load->library('form_validation');

$this->form_validation->set_rules('email', 'Email', 'required|valid_email');

if ($this->form_validation->run()) {
    // Process form
} else {
    // Show errors
}
```

---

### **8. How do sessions work in CodeIgniter?**

CodeIgniter uses its own **Session Library**:

```php
$this->load->library('session');

// Set session
$this->session->set_userdata('user_id', 123);

// Get session
$this->session->userdata('user_id');

// Remove session
$this->session->unset_userdata('user_id');
```

---

### **9. How do you implement pagination in CodeIgniter?**

```php
$this->load->library('pagination');

$config['base_url'] = base_url('users/index');
$config['total_rows'] = $this->User_model->get_count();
$config['per_page'] = 10;
$this->pagination->initialize($config);

$data['users'] = $this->User_model->get_users($config['per_page'], $this->uri->segment(3));
```

---

### **10. How do you send email in CodeIgniter?**

```php
$this->load->library('email');

$this->email->from('you@example.com', 'Your Name');
$this->email->to('someone@example.com');
$this->email->subject('Email Test');
$this->email->message('Testing email.');
$this->email->send();
```

---

### **11. What are hooks in CodeIgniter?**

Hooks allow you to run custom code **without modifying core files**, e.g., before/after controller execution.

Enable in `config/config.php`:

```php
$config['enable_hooks'] = TRUE;
```

Define hook in `application/config/hooks.php`.

---

### **12. How do you create and use custom libraries in CodeIgniter?**

**Steps:**

1. Create file: `application/libraries/MyLib.php`
2. Define class:

```php
class MyLib {
    public function sayHello() {
        return "Hello from library!";
    }
}
```

3. Load and use in controller:

```php
$this->load->library('MyLib');
echo $this->mylib->sayHello();
```

---

### **13. How do you upload files in CodeIgniter?**

```php
$this->load->library('upload');
$config['upload_path'] = './uploads/';
$config['allowed_types'] = 'jpg|png|pdf';
$this->upload->initialize($config);

if ($this->upload->do_upload('file')) {
    $data = $this->upload->data();
} else {
    $error = $this->upload->display_errors();
}
```

---

### **14. What is the difference between `$this->load->view()` and `redirect()`?**

* `$this->load->view()` loads a view file.
* `redirect()` sends an HTTP redirect to another URL.

```php
redirect('dashboard');
```

---

### **15. How do you handle 404 errors in CodeIgniter?**

In `application/config/routes.php`:

```php
$route['404_override'] = 'custom404';
```

Create `Custom404.php` controller and handle page not found.

---

## ✅ **Advanced CodeIgniter Interview Questions & Answers**

---

### **16. How do you build a REST API in CodeIgniter?**

You can use:

* CodeIgniter’s built-in routing + controllers
* Or a library like [`codeigniter-restserver`](https://github.com/chriskacerguis/codeigniter-restserver)

**Example (basic custom REST API):**

```php
// routes.php
$route['api/users/(:num)'] = 'api/users/id/$1';

// Controller: application/controllers/api/Users.php
class Users extends CI_Controller {
    public function id($id) {
        $this->load->model('User_model');
        $user = $this->User_model->get_user($id);
        echo json_encode($user);
    }
}
```

Set correct headers:

```php
header('Content-Type: application/json');
```

---

### **17. How do you secure your CodeIgniter application?**

* Use `xss_clean()` and `html_escape()` to sanitize input/output.
* Validate every input using `form_validation`.
* Use CSRF protection: enable it in `config/config.php`

  ```php
  $config['csrf_protection'] = TRUE;
  ```
* Store passwords using `password_hash()` and `password_verify()`.
* Sanitize URLs and use proper escaping in queries.
* Never expose error messages in production.

---

### **18. How do you extend core libraries in CodeIgniter?**

To override a core class (e.g., Email):

1. Create file: `application/libraries/MY_Email.php`
2. Class name must be prefixed with `MY_` (or your configured subclass prefix)

```php
class MY_Email extends CI_Email {
    public function custom_function() {
        // custom code
    }
}
```

---

### **19. How to implement multi-language support (i18n) in CodeIgniter?**

1. Create language files:
   `application/language/english/site_lang.php`

   ```php
   $lang['welcome'] = 'Welcome';
   ```

2. Load language:

   ```php
   $this->lang->load('site', 'english');
   echo $this->lang->line('welcome');
   ```

3. Dynamically set language via URL or session.

---

### **20. How do you enable CORS in CodeIgniter (for APIs)?**

In your controller or a helper file, set headers:

```php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");
```

For pre-flight `OPTIONS` handling:

```php
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    die();
}
```

---

### **21. How to use transactions in CodeIgniter?**

For atomic DB operations:

```php
$this->db->trans_start();
$this->db->insert('table1', $data1);
$this->db->insert('table2', $data2);
$this->db->trans_complete();

if ($this->db->trans_status() === FALSE) {
    // rollback
}
```

---

### **22. How do you cache pages in CodeIgniter?**

Enable output caching:

```php
$this->output->cache(10); // cache for 10 minutes
```

To delete cache:

```php
$this->output->delete_cache('controller/method');
```

Make sure cache is enabled in `config/config.php`.

---

### **23. How do you handle file downloads in CodeIgniter?**

```php
$this->load->helper('download');
force_download('path/to/file.pdf', NULL);
```

---

### **24. How to integrate AJAX with CodeIgniter?**

* Use jQuery or JavaScript `fetch()` to send AJAX request.
* Respond with JSON from your controller:

```php
$this->output
     ->set_content_type('application/json')
     ->set_output(json_encode(['status' => 'success']));
```

---

### **25. How do you optimize CodeIgniter performance?**

* Enable query caching (`$this->db->cache_on();`)
* Use output caching
* Minify assets (CSS/JS)
* Use database indexes
* Avoid loading unnecessary libraries/helpers
* Use profiler during development:

```php
$this->output->enable_profiler(TRUE);
```

---

### **26. How can you create reusable views/layouts (like master layout)?**

Create a base layout:

```php
// application/views/layouts/master.php
<html>
  <head><?php $this->load->view('partials/head'); ?></head>
  <body>
    <?php $this->load->view($page); ?>
  </body>
</html>
```

In controller:

```php
$data['page'] = 'pages/home';
$this->load->view('layouts/master', $data);
```

---

### **27. What are the most useful CodeIgniter helpers you've used?**

* `url_helper`: `base_url()`, `site_url()`
* `form_helper`: `form_open()`, `form_input()`
* `text_helper`: `word_limiter()`, `character_limiter()`
* `security_helper`: `xss_clean()`
* `download_helper`: `force_download()`

---

### **28. What is the difference between `base_url()` and `site_url()`?**

* `base_url()` returns the root URL (e.g., [https://site.com/](https://site.com/))
* `site_url()` includes the `index.php` (e.g., [https://site.com/index.php/controller/method](https://site.com/index.php/controller/method))

---

### **29. How to upload multiple files in CodeIgniter?**

Use a loop with `$_FILES` array:

```php
for ($i = 0; $i < count($_FILES['files']['name']); $i++) {
    $_FILES['file']['name'] = $_FILES['files']['name'][$i];
    // ... set other $_FILES fields
    $this->upload->do_upload('file');
}
```

---

### **30. How do you debug CodeIgniter applications?**

* Use `$this->output->enable_profiler(TRUE);`
* Enable error reporting:

```php
error_reporting(E_ALL);
ini_set('display_errors', 1);
```

* Use `log_message('error', 'Something went wrong');`

---

## ✅ **CodeIgniter HMVC Interview Questions & Answers**

---

### **1. What is HMVC in CodeIgniter?**

**HMVC** stands for **Hierarchical Model-View-Controller**. It’s an extension of MVC that allows you to **modularize** your application — meaning you can group related MVC components into self-contained **modules**.

> Each module in HMVC has its own models, views, and controllers, making your application more organized and scalable.

---

### **2. Why use HMVC in CodeIgniter?**

* **Better code organization** — especially for large apps
* **Reusable modules** — login, users, dashboard can be reused across projects
* **Separation of concerns** — each module is independent
* Helps **team collaboration** by breaking features into isolated modules

---

### **3. How do you enable HMVC in CodeIgniter?**

CodeIgniter doesn’t support HMVC natively. You need to use the **Modular Extensions - HMVC** by *wiredesignz*.

1. Download it from GitHub:
   [https://bitbucket.org/wiredesignz/codeigniter-modular-extensions-hmvc](https://bitbucket.org/wiredesignz/codeigniter-modular-extensions-hmvc)

2. Copy the files to your project:

   * Copy `MX/` folder into `application/third_party/`
   * Replace your `CI_Controller` with `MX_Controller` in controllers

---

### **4. What is MX\_Controller?**

`MX_Controller` is an extension of `CI_Controller` provided by Modular Extensions – HMVC. It adds support for loading **modules within modules** and supports calling controllers as widgets (like a view).

Example:

```php
class Dashboard extends MX_Controller {
    public function index() {
        $this->load->module('auth');
        $this->auth->check_login();
    }
}
```

---

### **5. What is the typical folder structure for an HMVC module?**

```
application/
├── modules/
│   ├── users/
│   │   ├── controllers/
│   │   │   └── Users.php
│   │   ├── models/
│   │   │   └── User_model.php
│   │   ├── views/
│   │   │   └── user_list.php
```

---

### **6. How do you load a controller from another module in HMVC?**

```php
$this->load->module('users');
$this->users->index(); // Call index method of Users controller
```

---

### **7. How do you load a view from a module in HMVC?**

```php
$this->load->view('users/user_list'); // assuming inside modules/users/views/
```

Or use:

```php
echo Modules::run('users/user_list');
```

---

### **8. What is `Modules::run()` in HMVC?**

It allows you to call a controller **as a widget/component**.
This is useful when you want to render a part of another controller’s output in a view.

Example:

```php
echo Modules::run('auth/login_box');
```

---

### **9. Can modules in HMVC call each other?**

Yes. Since each module is a self-contained unit, one module can load another module’s controller or model via:

```php
$this->load->module('module_name');
```

---

### **10. What are real-life use cases of HMVC?**

* Admin panels with modules like `dashboard`, `users`, `settings`
* Frontend websites with independent sections: `home`, `blog`, `gallery`
* Multitenant apps where each client/tenant loads its own module

---

### **11. What are the downsides of using HMVC?**

* Slight performance overhead due to module loading
* Can add complexity if not structured properly
* Not officially supported by CodeIgniter core (needs 3rd party)

---

### **12. How do you organize a reusable module in CodeIgniter HMVC?**

You can create a module like `auth` with login, registration, and access control. Use:

* `modules/auth/controllers/Auth.php`
* `modules/auth/models/Auth_model.php`
* `modules/auth/views/login_form.php`

And call:

```php
Modules::run('auth/login_form');
```

---

