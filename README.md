![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Mini Project | Vikings

## Introduction

The Vikings and the Saxons are at War. Both are Soldiers but they have their own methods to fight. Vikings are ported to Python. YAY!!

In this laboratory we worked with the concept of **inheritance** in Python.

### Getting Started

The following files can be found in the folder for this laboratory:

- `vikingsClasses.py`
- `1-testSoldier.py`
- `2-testVikings.py`
- `3-testSaxons.py`
- `4-testWar.py`
- `wargame.py`
  

### Challenge Question

Our task was to modify the file `vikingsClasses.py` so that all the tests were correct.

## Exercise

![](https://i.imgur.com/5TPElt8.jpg)

---

The starter code in the file is the following:

```
# Soldier
class Soldier:

# Viking
class Viking:

# Saxon
class Saxon:

# War
class War:
```

In this case, the test says that _Soldier constructor function should receive 2 arguments (health & strength)_, so we had to write the correct code.
Then, the Viking and Saxon classes are actually subclasses of soldiers, so we applied the concept of **inheritance**, having both these classes inheriting the methods defined for the Soldier class.

### Soldier

The `Soldier` constructor function has 2 methods: `attack()` and `receiveDamage()`, and receives **2 arguments** (health & strength)


#### The `attack()` method receives no arguments and returns **the `strength` property of the `Soldier`**


#### The `receiveDamage()` method receives **1 argument** (the damage) and removes the received damage from the `health` property


---

### Viking

A `Viking` is a `Soldier` with an additional property, their `name`. They have a different `receiveDamage()` method and new method, `battleCry()`.

The `Viking` constructor function inherits from `Soldier`, receives **3 arguments** (name, health & strength) and has 2 methods: `attack()` and a modified `receiveDamage()`.


#### The `attack()` method is **inherited** from `Soldier`.

#### The `receiveDamage()` method has been **reimplemented** for `Viking` to make the `Viking` version have different return values.
##### It still receives **1 argument** (the damage) and removes the received damage from the `health` property.
##### An extra step for this method is that it checks weather or not the `Viking` is still alive and either returns the amount of damage the `Viking`has taken, or the information that the `Viking` has died.

##### The `battleCry()` method just returns a specified battlecry (**"Odin Owns You All!"**)

---

### Saxon

A `Saxon` is a weaker kind of `Soldier`. Unlike a `Viking`, a `Saxon` has no name. They also have a different `receiveDamage()` method.

The `Saxon` constructor function inherits from `Soldier`, receives **2 arguments** (health & strength) and has 2 methods: `attack()` and a modified `receiveDamage()`.


#### The `attack()` method is **inherited** from `Soldier`.

#### The `receiveDamage()` method has been **reimplemented** for `Saxon` to make the `Saxon` version have different return values.
##### It still receives **1 argument** (the damage) and removes the received damage from the `health` property.
##### An extra step for this method is that it checks weather or not the `Saxon` is still alive and either returns the amount of damage the `Saxon`has taken, or the information that the `Saxon` has died.

---

### War

Now we get to the good stuff: WAR! Our `War` constructor function allows us to have a `Viking` army and a `Saxon` army that battle each other.

The `War` constructor has 5 methods:

- `addViking()`
- `addSaxon()`
- `vikingAttack()`
- `saxonAttack()`
- `showStatus()`

When we first create a `War`, the armies are empty. We will add soldiers to the armies later.


#### The `addViking()` method adds 1 `Viking` to the `vikingArmy`.
##### It receives **1 argument** (a `Viking` object) and adds the received `Viking` to the army


#### The `addSaxon()` method adds 1 `Saxon` to the `saxonArmy`.
##### It receives **1 argument** (a `Saxon` object) and adds the received `Saxon` to the army


#### `vikingAttack()` method

A `Saxon` (chosen at random) has their `receiveDamage()` method called with the damage equal to the `strength` of a `Viking` (also chosen at random). This will only perform a single attack and the `Saxon` doesn't get to attack back.
##### It removes dead saxons from the army, and returns the result of calling the `receiveDamage()` method on a `Saxon`.


#### `saxonAttack()` method

A `Viking` (chosen randomly) receives the damage equal to the `strength` of a random attacking `Saxon`.
##### It removes dead vikings from the army, and returns the result of calling the `receiveDamage()` method on a `Viking`.


#### `showStatus()` method

Returns the current status of the `War` based on the size of the armies.