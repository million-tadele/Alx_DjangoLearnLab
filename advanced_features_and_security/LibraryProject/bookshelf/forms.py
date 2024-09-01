<!-- form_example.html -->
<form method="post" action="/submit/">
    {% csrf_token %}
    <!-- form fields here -->
    <button type="submit">Submit</button>
</form>
