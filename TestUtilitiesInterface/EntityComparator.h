#pragma once

#include "EntityComparatorConfiguration.h"

#include <gtest/gtest.h>
#include <gmock/gmock.h>


using namespace testing;
namespace systelab { namespace test_utility {

	class EntityComparator
	{
	public:
		EntityComparator(const EntityComparatorConfiguration& configuration = EntityComparatorConfiguration())
			:m_configuration(configuration)
		{}

		template <typename _Entity>
		testing::AssertionResult operator() (const _Entity& expected, const _Entity& actual) const;

	protected:
		EntityComparatorConfiguration m_configuration;
	};

}}

// Macro that declares a matcher that compares the passed value with a specific entity using an EntityComparator
MATCHER_P(isEqTo, expectedEntity, "EntityComparison") \
	{ \
		AssertionResult rc = systelab::test_utility::EntityComparator()(expectedEntity, arg); \
		*result_listener << rc.message(); \
		return rc; \
	};

// Macro that declares a matcher that compares the passed value with a specific entity using an EntityComparator
MATCHER_P2(isEqTo, expectedEntity, comparatorConfiguration, "EntityComparison") \
	{ \
		AssertionResult rc = systelab::test_utility::EntityComparator(comparatorConfiguration)(expectedEntity, arg); \
		*result_listener << rc.message(); \
		return rc; \
	};
