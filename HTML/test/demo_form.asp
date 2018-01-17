<body>
	服务器接收到的用户输入为:
	<%
	response.write(request.form("name"))
	%>
</body>