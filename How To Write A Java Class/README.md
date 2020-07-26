_I completed it when I didn't know what to do last night._
# How To Write A Java Class
## What is it used for?
To create a very simple `java` file from a `text` file, like that:<br>
<br>
```text
Dog
-name:String
-age:int
Dog()
Dog(name:String)
+getName():String
+getAge():int
+setName(name:String)
+bark()

```
to
```java
class Dog {

	private String name;
	private int age;

	Dog() { }

	Dog(String name) { }

	public String getName() { }

	public int getAge() { }

	public void setName(String name) { }

	public void bark() { }

}
```
## How to use it?
Write in `input.txt` and don't forget to `save` it, we have some rules:<br>
* The first line must be `class name`
* Change `access modifier` of `attribute` and `method` by adding to the beginning of the line:
  * `+` as `public`
  * `-` as `private`
  * it will be `default` if you add nothing
* `name` and `data type` of an `attribute` are separated by a colon (`:`)
* `parameters` of a `method` are written in parentheses (`(` and `)`) after the `name`:
  * `name` and `data type` of each `parameter` are separated by a colon (`:`)
  * `parameters` are seperated by a comma (`,`)
* `data type` of `method` is written at the end, after the colon (`:`)

Run `main.py` by running this command-line in your `terminal` or `command prompts`: `python3 main.py` or `python main.py`.<br>
Check `output.java` out!<br>

# Hope you like it!

