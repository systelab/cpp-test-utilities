# C++ Test Utilities interface

This repository contains a common interface for the test utilities used by the different Systelab projects.

## Usage

### Entity comparators

Entity comparators allow adding an equality expectation for Google Test over two model entities. When the entities are different, the comparator will  provide a detailed message with the first difference found. So, they are very useful for troubleshooting failures on unit tests or integration tests.

For instance, given a `Patient` model entity:

```cpp
struct Patient
{
    std::string name;
    int age;
    bool male;
};
```

An entity comparator can be defined by implementing the `operator()`:

```cpp
namespace systelab { namespace test_utility {

    template <>
    testing::AssertionResult EntityComparator::operator() (const Patient& expected, const Patient& actual) const
    {
        if (expected.name != actual.name)
        {
            return AssertionFailure() << "Different value for name: expected=" << expected.name
                                      << ", actual=" << actual.name;
        }

        if (expected.age != actual.age)
        {
            return AssertionFailure() << "Different value for age: expected=" << expected.age
                                      << ", actual=" << actual.age;
        }

        ...

        return AssertionSuccess();
    }
```

Then it can be used on a unit test as follows:

```cpp
TEST_F(PatientTest, testPatientsAreEqual)
{
    Patient expectedEntity = {"Nicolas Cage", 55, true};
    Patient actualEntity = {"Nicolas Cage", 51, true};
    ASSERT_TRUE(systelab::test_utility:EntityComparator()(expectedEntity, actualEntity));
}
```

The standard output for the previous test should be something like:

```cpp
`TBD
```



