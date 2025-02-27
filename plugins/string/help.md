# Description

The String Operations plugin allows easy manipulation of string data.

This plugin utilizes the Python 3 String library [set of methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

# Key Features

* Split a string to a list of elements
* Split a string to an object
* Upper case, lower case, and trim a string
* Replace parts of a string

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Replace

This action is used to replace parts of a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|in_string|string|None|True|The string to replace parts of|None|this is a string|
|replacement_value|string|None|False|The string that will replace the parts that are found. If left blank the characters to find will be deleted|None|replacement|
|string_part_to_find|string|None|True|The string part to look for. All instances of this string will be replaced|None|string|

Example input:

```
{
  "in_string": "the cow jumped over the moon",
  "replacement_value": "cat",
  "string_part_to_find": "cow"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result_string|string|True|The string after replacement|

Example output:

```
{
  "result_string": "the cat jumped over the moon"
}
```

#### Length

This action is used to return the length of a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|string|string|None|True|String to return length of|None|return the number of characters in this string|

Example input:

```
{
  "string": "return the number of characters in this string"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|length|integer|True|Length of string|

Example output:

```
{
  "length": 46
}
```

#### Split String to List

This action is used to convert a string to a list of strings.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|delimiter|string|None|False|The character used to split the string into slices for the list. The default is a newline, if not provided by the user|None|,|
|string|string|None|True|String to break into an array|None|This,is,a,sentence|

Example input:

```
{
  "delimiter": ",",
  "string": "This,is,a,sentence"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]string|False|List of string components|

Example output:

```
{
  "list": [
    "This",
    "is",
    "a",
    "sentence"
  ]
}
```

#### Split String to Object

This action is used to convert a string to an object containing key:value strings.

Any input requiring more than a single key:value pair, e.g. `USER=Bob` needs to use the `block_delimiter` option.
In this case, the input string is split by the `block_delimiter` character first, and the resulting items are then split
by the `string_delimiter` option. Stripping of double-quotes is automatically applied in this situation for each item before the plugin returns it.

The [output schema object](https://docs.komand.com/v0.42.1/docs/python-script-plugins#section-configure-the-plugin-output-schema) on the action's page can be modified to pre-populate the workflow with the names of the keys.
It allows users the ability to use the green selector and choose a specific variable later in the workflow by name.
[Input templating](https://docs.komand.com/docs/input-templating) would need to be used to obtain variables by name otherwise.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|block_delimiter|string|None|False|The character delimiter for the initial string split, applied before the string delimiter input. This parameter is optional but allows for more complex handling|None|[|
|string|string|None|True|String to convert e.g. USER=Bob|None|User=Bob|
|string_delimiter|string|None|False|The character used to split the string into slices for the list. The default is a space, if not provided by the user|None|=|

Example input:

```
{
  "string": "User=Bob",
  "string_delimiter": "="
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|object|object|False|Object from string split|

Given an input string of `User=Bob`, setting `string_delimiter` to `=` would return the information presented in the example below.

Example output:

```
{
  "object": {
    "User": "Bob"
  }
}
```

Here is another example with a slightly more complex string input that contains multiple key:value pairs.
These pairs are separated from each other by a space, and the keys and values within each pair are separated by an equal sign:

```
Computer_ID="bef41e8b-47b8-e188-8e43-3a2b662dd55d" Computer_Name="dgdemo\RGWin64" Computer_Type="Windows"
```

Setting `block_delimiter` to ` ` and `string_delimiter` to `=` will return the information presented in the example below.

Example output:

```
{
  "object": {
    "Computer_ID": "bef41e8b-47b8-e188-8e43-3a2b662dd55d",
    "Computer_Name": "dgdemo\RGWin64",
    "Computer_Type": "Windows"
  }
}
```

#### Upper

This action is used to convert lowercase letters to uppercase.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|string|string|None|True|String to uppercase|None|uppercase this string|

Example input:

```
{
  "string": "uppercase this string"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|upper|string|False|Uppercase string|

Example output:

```
{
  "upper": "UPPERCASE THIS STRING"
}
```

#### Lower

This action is used to convert uppercase letters to lowercase.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|string|string|None|True|String to convert e.g. USER=bob|None|LOWERCASE THIS STRING|

Example input:

```
{
  "string": "LOWERCASE THIS STRING"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|lower|string|False|Lowercase string|

Example output:

```
{
  "lower": "LOWERCASE THIS STRING"
}
```

#### Set Encoding

This action is used to encode a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encoding|string|None|True|Encoding to use|['UTF-8', 'ASCII']|ASCII|
|error_handling|string|None|True|Error handler to use for encoding and decoding|['strict', 'replace', 'ignore']|ignore|
|string|string|None|True|String to encode|None|hello|

Example input:

```
{
  "encoding": "ASCII",
  "error_handling": "ignore",
  "string": "hello"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|encoded|string|True|Encoded string|

Example output:

```
{
  "encoded": "hello"
}
```

#### Trim

This action is used to trim a string of leading and trailing whitespace.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|string|string|None|True|String to trim|None|Extra spaces at the end of this string     |

Example input:

```
{
  "string": "Extra spaces at the end of this string     "
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|trimmed|string|True|Trimmed string|

Example output:

```
{
  "trimmed": "Extra spaces at the end of this string"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

There may be complex string manipulation needs that are likely outside the scope of this plugin.
If this is the case, consider using the Python 3 Script plugin instead.

# Version History

* 1.4.0 - New action Replace
* 1.3.1 - Update to v4 Python plugin runtime
* 1.3.0 - New action Length | Add example inputs
* 1.2.1 - New spec and help.md format for the Extension Library
* 1.2.0 - New action Trim
* 1.1.0 - New action Set Encoding
* 1.0.1 - Update plugin tag from `util` to `utilities` for Marketplace searchability
* 1.0.0 - Initial plugin

# Links

## References

* [Python 3 String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
