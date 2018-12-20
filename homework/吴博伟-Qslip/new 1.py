pd.concat
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
	objs：Series，DataFrame或Panel对象的序列或映射。如果传递了dict，则排序的键将用作键参数，除非它被传递，在这种情况下，将选择值（见下文）。任何无对象将被静默删除，除非它们都是无，在这种情况下将引发一个ValueError。
	axis：{0,1，...}，默认为0。沿着连接的轴。
	join：{'inner'，'outer'}，默认为“outer”。如何处理其他轴上的索引。outer为联合和inner为交集。
	ignore_index：boolean，default False。如果为True，请不要使用并置轴上的索引值。结果轴将被标记为0，...，n-1。如果要连接其中并置轴没有有意义的索引信息的对象，这将非常有用。注意，其他轴上的索引值在连接中仍然受到尊重。
	join_axes：Index对象列表。用于其他n-1轴的特定索引，而不是执行内部/外部设置逻辑。
	keys：序列，默认值无。使用传递的键作为最外层构建层次索引。如果为多索引，应该使用元组。
	levels：序列列表，默认值无。用于构建MultiIndex的特定级别（唯一值）。否则，它们将从键推断。
	names：list，default无。结果层次索引中的级别的名称。
	verify_integrity：boolean，default False。检查新连接的轴是否包含重复项。这相对于实际的数据串联可能是非常昂贵的。
	copy：boolean，default True。如果为False，请勿不必要地复制数据
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
   ...:                     'B': ['B0', 'B1', 'B2', 'B3'],
   ...:                     'C': ['C0', 'C1', 'C2', 'C3'],
   ...:                     'D': ['D0', 'D1', 'D2', 'D3']},
   ...:                     index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
   ...:                     'B': ['B4', 'B5', 'B6', 'B7'],
   ...:                     'C': ['C4', 'C5', 'C6', 'C7'],
   ...:                     'D': ['D4', 'D5', 'D6', 'D7']},
   ...:                      index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
   ...:                     'B': ['B8', 'B9', 'B10', 'B11'],
   ...:                     'C': ['C8', 'C9', 'C10', 'C11'],
   ...:                     'D': ['D8', 'D9', 'D10', 'D11']},
   ...:                     index=[8, 9, 10, 11])
frames = [df1, df2, df3]
In [5]: result = pd.concat(frames)
KEY参数:
	result = pd.concat(frames, keys=['x', 'y', 'z'])
JOIN参数
	join = 'inner'，则说明为取交集
	join = 'outer',为取并集的关系
pd.merge
	merge的参数
	一次组合多个dataframe的时候可以传入元素为dataframe的列表或者tuple。一次join多个，一次解决多次烦恼~
	on：列名，join用来对齐的那一列的名字，用到这个参数的时候一定要保证左表和右表用来对齐的那一列都有相同的列名。
	left_on：左表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。
	right_on：右表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。
	left_index/ right_index: 如果是True的haunted以index作为对齐的key
	how：数据融合的方法。：left right outer inner
	sort：根据dataframe合并的keys按字典顺序排序，默认是，如果置false可以提高表现。
	suffix后缀参数：如果和表合并的过程中遇到有一列两个表都同名，但是值不同，合并的时候又都想保留下来，
					就可以用suffixes给每个表的重复列名增加后缀
merge的默认合并方法：
	merge用于表内部基于 index-on-index 和 index-on-column(s) 的合并，但默认是基于index来合并。
更新表的nan值：
	combine_first：如果一个表的nan值，在另一个表相同位置（相同索引和相同列）可以找到，则可以通过combine_first来更新数据
	update：如果要用一张表中的数据来更新另一张表的数据则可以用update来实现
	combine_first 和 update 的区别：
		使用combine_first会只更新左表的nan值。而update则会更新左表的所有能在右表中找到的值（两表位置相对应）。


	
to_datatime
df.resample('')