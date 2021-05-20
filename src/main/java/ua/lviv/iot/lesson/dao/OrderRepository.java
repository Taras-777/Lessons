package ua.lviv.iot.lesson.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import ua.lviv.iot.lesson.models.Order;

@Repository
public interface OrderRepository extends JpaRepository<Order, Integer> {
}
