package ua.lviv.iot.lesson.services;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import ua.lviv.iot.lesson.dao.OrderRepository;
import ua.lviv.iot.lesson.exception.OrderNotFoundException;
import ua.lviv.iot.lesson.models.Order;

import java.util.List;

@Service
public class OrderService {

    private final OrderRepository orderRepository;

    @Autowired
    public OrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    public Order addOrder(Order order) {
        return orderRepository.save(order);
    }

    public Order updateOrder(Order order) throws OrderNotFoundException {

        if (orderRepository.existsById(order.getId())) {
            return orderRepository.save(order);
        }
        throw new OrderNotFoundException("Order with id: " + order.getId() + "not found");
    }

    public List<Order> getOrders() {
        return orderRepository.findAll();
    }

    public Order getOrder(Integer id) {
        return orderRepository.findById(id).orElseThrow();
    }
}
