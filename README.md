# Xây dựng ODS phục vụ cho report dữ liệu bán lẻ real-time


Dự án này được dùng để so sánh với StarRocks: [https://github.com/spaghetti-lover/viettel-ods-](https://github.com/spaghetti-lover/viettel-ods-starrocks)
## Cách chạy:
**Điều kiện**: Cài đặt Docker và docker-compose

**Bước 1: Clone dự án**:
1. Mở terminal
2. Clone dự án:
```
https://github.com/spaghetti-lover/viettel-ods-clickhouse.git
```

**Bước 2: Vào dự án**
1. Vào thư mục gốc của dự án:
```
cd viettel-ods-clickhouseclickhouse
```

**Bước 3: Chạy Docker Containers**
1. Chạy file docker-compose:
```
docker-compose up
```

**Bước 4: Check các service khởi tạo**
1. Trong quá trình khởi động các service, check log để xem các service khởi động thành công chưa
2. Chú ý tới `airflow-init` và `debezium-init` containers. Hai cái này sẽ tắt khi nào chạy xong
3. Đảm bảo các service còn lại chạy thành công


**Bước 5: Truy cập vào các service**
   - **Airflow UI:** `http://localhost:13005` username:`airflow`, password:`airflow`
   - **Debezium UI:** `http://localhost:8085` _(authentication not required)_
   - **Kafka UI:** `http://localhost:8095/` _(authentication not required)_
   - **Grafana Dashboard:** `http://localhost:13000` username:`admin`, password:`admin`
   - **PostgreSQL:** port:`65432`, username:`postgres`, password:`postgres`
   - **ClickHouse:** port:`8123`, username:`default`, password: _(not required)_

