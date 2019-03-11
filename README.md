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
    double height;
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
    Patient expectedEntity = {"Nicolas Cage", 55, 1.81, true};
    Patient actualEntity = {"Nicolas Cage", 51, 1.81, true};
    ASSERT_TRUE(systelab::test_utility:EntityComparator()(expectedEntity, actualEntity));
}
```

The execution of this test should print something like:

```cpp
Different value for age: expected=55, actual=51
```

#### Helper macros

Boilerplate code on `EntityComparator` implementations can be reduced significantlly by using some helper macros. They allow performing simple comparisons within a single line of code:

```cpp
COMPARATOR_ASSERT_EQUAL(expected, actual, name); // Compares an expression result by asserting it to be equal
COMPARATOR_ASSERT_EQUAL(expected, actual, age); 
COMPARATOR_ASSERT_EQUAL(expected, actual, male);
COMPARATOR_ASSERT_NEAR(expected, actual, height, 1e-4);  // Compares an expression result by asserting it to be near
                                                         // (using a given tolerance)
```
