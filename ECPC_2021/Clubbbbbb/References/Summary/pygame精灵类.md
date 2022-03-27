pygame精灵类
==========



- pygame.sprite.Sprite 拥有以下方法：

- update

  > update(*args, **kwargs) -> None 相当于一个接口而已

- add

  > add(*groups) -> None 将该sprite加入到groups的所有group中。 *remove
  > remove(*groups) -> None 同理

- kill

  > kill() -> None 将该sprite从所有group中移除

- alive

  > alive() -> bool 如果该sprite属于任何group，返回True

- groups

  > groups() -> group_list 返回所有含有该sprite的group

- pygame.sprite.Group

  > 创建一个组，用于存储sprite

- pygame.sprite.SingleGroup

  > 创建一个只能有一个对象的组，一旦新的对象被加进去，旧的将被移除

有关sprite碰撞相关知识，参见 [碰撞检测](https://www.ecpc.top/ECPC_2021/Clubbbbbb/Lecture3/碰撞检测.html)

