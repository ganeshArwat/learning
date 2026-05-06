# SETUP CRON JOB FOR A COMPANY

## STEP 1: ADD CRON JOB IN THE DATABASE

- login to the phpmyadmin according domain dns ip

- in the trackmate_lite database, add the following cron job in the cron_jobs table

- replace <COMPANY_ID> with the company id

```sql
INSERT INTO `cron_jobs` (`id`, `company_id`, `job_name`, `cron_url`, `cron_expression`, `next_run_at`, `last_run_at`, `status`, `retry_count`, `max_retries`, `created_at`) VALUES 
(NULL, <COMPANY_ID>, 'refresh_awb', 'cron/refresh_docket/refresh_awb', '*/5 * * * *', NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'refresh_sales', 'cron/refresh_docket/refresh_sales', '*/5 * * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'refresh_purchase', 'cron/refresh_docket/refresh_purchase', '*/5 * * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'refresh_delivery', 'cron/refresh_docket/refresh_delivery', '*/5 * * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_mis_6_am', 'cron/customer_mis/insert_custom_report_email', '45 5 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_mis_8_am', 'cron/customer_mis/insert_custom_report_email', '45 7 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_mis_11_pm', 'cron/customer_mis/insert_custom_report_email', '45 10 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_mis_2_pm', 'cron/customer_mis/insert_custom_report_email', '45 13 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_mis_4_pm', 'cron/customer_mis/insert_custom_report_email', '45 15 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_mis_7_pm', 'cron/customer_mis/insert_custom_report_email', '45 18 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'send_report_email', 'cron/customer_mis/send_report_email', '*/30 * * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'customer_outstanding', 'cron/customer_outstanding/insert_custom_report_email', '0 4 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'outstanding_email', 'cron/outstanding_email/send_outstanding_email', '50 9 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'update_closing_bank_balance', 'cron/bank_balance/update_closing_balance', '22 1 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'lock_all_invoice', 'cron/lock_all_invoice/lock_all_invoice', '30 2 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'docket_report', 'cron/docket_report/send_docket_email', '5 9 * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP),
(NULL, <COMPANY_ID>, 'sync_cron_tracking', 'cron/refresh_docket/sync_cron_tracking', '*/5 * * * *',  NULL, NULL, 'active', '0', '3', CURRENT_TIMESTAMP);
```


## STEP 2: RUN THE HTTP URL (SCRIPT) TO UPDATE THE NEXT RUN TIME
- change the IP to the IP of the server
```bash
http://<IP>/cron/cron_scheduler/updateNextRun
```
- after running the script, check the next_run_at column in the cron_jobs table with company id <COMPANY_ID> should be updated
```sql
SELECT * FROM `cron_jobs` WHERE `company_id` = <COMPANY_ID>
```

## STEP 3: ADD CRON JOB IN THE SERVER To Start the Cron Worker

- replace <COMPANY_ID> with the company id
- login to the server using ssh

- open crontab file

```bash
sudo crontab -e
```

- add the following cron line to the crontab file
```bash
* * * * * COMPANY_ID=<COMPANY_ID> /usr/bin/php /var/www/html/trackmate_lite/index.php cron/cron_worker_new run_once >> /var/www/html/trackmate_lite/ci_worker/cron_worker_<COMPANY_ID>.log 2>&1
```