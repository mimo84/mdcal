# mdcal

Generate calendar in Markdown table.
Forked from: https://github.com/pn11/mdcal

## Difference with the original:

It generates links to a calendar markdown file for each day. The calendar part is hardcoded as:
`./calendar/year/month/day.md`.

It is also possible to generate the markdown days for each day by flipping the `write_md_days` to `True`.

## Usage

### Generate calendar of current month:

```sh
$ python3 mdcal.py
```

### Generate calendar of specified year:

```sh
$ python3 mdcal.py 2019
```

### Generate calendar of specified month:

```sh
$ python3 mdcal.py 1970 1
```

## Rendered Example

2022/6

|            Lunedì             |            Martedì            |           Mercoledì           |            Giovedì            |            Venerdì            |            Sabato             |           Domenica            |
| :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: |
| [30](./calendar/2022/5/30.md) | [31](./calendar/2022/5/31.md) |  [1](./calendar/2022/6/1.md)  |  [2](./calendar/2022/6/2.md)  |  [3](./calendar/2022/6/3.md)  |  [4](./calendar/2022/6/4.md)  |  [5](./calendar/2022/6/5.md)  |
|  [6](./calendar/2022/6/6.md)  |  [7](./calendar/2022/6/7.md)  |  [8](./calendar/2022/6/8.md)  |  [9](./calendar/2022/6/9.md)  | [10](./calendar/2022/6/10.md) | [11](./calendar/2022/6/11.md) | [12](./calendar/2022/6/12.md) |
| [13](./calendar/2022/6/13.md) | [14](./calendar/2022/6/14.md) | [15](./calendar/2022/6/15.md) | [16](./calendar/2022/6/16.md) | [17](./calendar/2022/6/17.md) | [18](./calendar/2022/6/18.md) | [19](./calendar/2022/6/19.md) |
| [20](./calendar/2022/6/20.md) | [21](./calendar/2022/6/21.md) | [22](./calendar/2022/6/22.md) | [23](./calendar/2022/6/23.md) | [24](./calendar/2022/6/24.md) | [25](./calendar/2022/6/25.md) | [26](./calendar/2022/6/26.md) |
| [27](./calendar/2022/6/27.md) | [28](./calendar/2022/6/28.md) | [29](./calendar/2022/6/29.md) | [30](./calendar/2022/6/30.md) |  [1](./calendar/2022/7/1.md)  |  [2](./calendar/2022/7/2.md)  |  [3](./calendar/2022/7/3.md)  |
